import pytest


@pytest.fixture
def mocker_item_id():
    """mock id"""
    return "lol"


@pytest.fixture
def mocker_dict_items(mocker_item_id):
    """mock """
    return {"item_id": mocker_item_id}


@pytest.fixture
def mocker_create_item():
    items = {
        "name": "Foo",
        "description": "lol",
        "price": 35.4,
        "tax": 3.2,
    }
    return items
