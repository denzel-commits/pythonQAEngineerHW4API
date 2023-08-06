import pytest
import requests
from configuration import OPEN_BREWERY_API_URL


def brewery_single_by_id(id_):
    return requests.get(f"{OPEN_BREWERY_API_URL}/breweries/{id_}")


def brewery_by_ids(ids):
    params = {"by_ids": ids}
    return requests.get(f"{OPEN_BREWERY_API_URL}/breweries", params=params)


def brewery_by_type(brewery_type):
    params = {"by_type": brewery_type}
    return requests.get(f"{OPEN_BREWERY_API_URL}/breweries", params=params)


@pytest.fixture
def get_single_brewery():
    return brewery_single_by_id


@pytest.fixture
def get_brewery_by_type():
    return brewery_by_type


@pytest.fixture
def get_brewery_by_ids():
    return brewery_by_ids
