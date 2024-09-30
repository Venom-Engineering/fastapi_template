from fastapi import APIRouter
from schema import schema

router = APIRouter(prefix="/subapp_1", tags=["subapp_1"])


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@router.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@router.get("/models/{model_name}")
async def get_model(model_name: schema.ModelName):
    if model_name is schema.ModelName.ALEXNET:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == schema.ModelName.RESNET:
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}