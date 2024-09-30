import pytest
from app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_sub_app_root():
    response = client.get("/subapp_1/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_sub_app_read_user_me():
    response = client.get("/subapp_1/users/me")
    assert response.status_code == 200
    assert response.json() == {"user_id": "the current user"}


def test_sub_app_read_items(mocker_item_id, mocker_dict_items):
    response = client.get(f"/subapp_1/items/{mocker_item_id}")
    assert response.status_code == 200
    assert response.json() == mocker_dict_items


@pytest.mark.parametrize(
    "value,output",
    [
        ("alexnet", {"model_name": "alexnet", "message": "Deep Learning FTW!"}),
        ("resnet", {"model_name": "resnet", "message": "LeCNN all the images"}),
        ("lenet", {"model_name": "lenet", "message": "Have some residuals"}),
    ],
)
def test_sub_app_get_model(value, output):
    response = client.get(f"/subapp_1/models/{value}")
    assert response.status_code == 200
    assert response.json() == output


def test_create_items(mocker_create_item):
    response = client.post(
        "/subapp_1/items_post",
        json=mocker_create_item,
    )
    assert response.status_code == 200
    assert response.json() == mocker_create_item
