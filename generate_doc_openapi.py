from pathlib import Path

import yaml
from app import app
from fastapi.openapi.utils import get_openapi

CURRENT_PATH = Path(__file__).resolve().parent
PATH_TO_DOC_FOLDER = CURRENT_PATH / "docs" / "app"
PATH_TO_DOC_SWAGGER = PATH_TO_DOC_FOLDER / "openapi.yaml"

if not PATH_TO_DOC_FOLDER.exists():
    PATH_TO_DOC_FOLDER.mkdir(parents=True)

with PATH_TO_DOC_SWAGGER.open(mode="w") as f:
    yaml.dump(
        get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
        ),
        f,
    )
