from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Ecommerce Backend"
    APP_VERSION: str = "1.0.0"

    POSTGRES_URL: str
    REDIS_URL: str

    JWT_SECRET: str
    JWT_ALGORITHM: str 
    JWT_EXPIRE_MINUTES: int 

    # ALLEGRO_CLIENT_ID: str | None = None
    # ALLEGRO_CLIENT_SECRET: str | None = None
    # ALLEGRO_REDIRECT_URI: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
