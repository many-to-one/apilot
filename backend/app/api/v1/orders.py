from fastapi import APIRouter, Depends
from app.dependencies import get_current_user
from app.services.sync_service import trigger_orders_sync

router = APIRouter()

@router.post("/sync")
async def sync(integration: str, account_id: int, user=Depends(get_current_user)):
    return await trigger_orders_sync(integration, account_id)
