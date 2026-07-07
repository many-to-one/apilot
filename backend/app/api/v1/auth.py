from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_session
from models.user import User
from core.security import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/register")
async def register(data: dict, db: AsyncSession = Depends(get_session)):
    email = data["email"]
    password = data["password"]

    existing = await db.execute(
        select(User).where(User.email == email)
    )
    if existing.scalar():
        raise HTTPException(400, "Email exists")

    user = User(email=email, hashed_password=hash_password(password))
    db.add(user)
    await db.commit()

    token = create_access_token(str(user.id))
    return {"access_token": token}

@router.post("/login")
async def login(
    form: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_session),
):
    result = await db.execute(select(User).where(User.email == form.username))
    user = result.scalar()

    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(401, "Invalid credentials")

    token = create_access_token(str(user.id))
    return {"access_token": token}
