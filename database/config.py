from typing import List

from database.settings import settings

MODELS_MODULES: List[str] = [
    "database.models.dummy_model",
    "database.models.attendance",
    "database.models.camera",
    "database.models.face",
    "database.models.intruderlog",
    "database.models.person",
    "database.models.user",
    "database.models.zone",
    "aerich.models"
]  # noqa: WPS407

TORTOISE_CONFIG = {  # noqa: WPS407
    "connections": {
        "default": str(settings.db_url),
    },
    "apps": {
        "models": {
            "models": MODELS_MODULES,
            "default_connection": "default",
        },
    },
}
