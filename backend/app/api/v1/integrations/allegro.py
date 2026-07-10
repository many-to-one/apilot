from fastapi import APIRouter
from api.v1.integrations._allegro.sdk.output.openapi_client.configuration import Configuration


router = APIRouter()

@router.get("/check")
async def check_connection():
    try:
        # Próba stworzenia konfiguracji SDK
        config = Configuration()

        # Minimalny test: sprawdzamy, czy SDK ma podstawowe elementy
        required_attrs = [
            "host",
            "access_token",
            "api_key",
            "api_key_prefix",
        ]

        missing = [attr for attr in required_attrs if not hasattr(config, attr)]

        if missing:
            return {
                "status": "error",
                "message": "SDK Allegro jest niekompletne lub uszkodzone.",
                "missing_attributes": missing,
            }

        return {
            "status": "ok",
            "message": "SDK Allegro działa poprawnie. Możesz kontynuować integrację.",
        }

    except Exception as e:
        return {
            "status": "error",
            "message": "SDK Allegro nie działa poprawnie.",
            "details": str(e),
        }
