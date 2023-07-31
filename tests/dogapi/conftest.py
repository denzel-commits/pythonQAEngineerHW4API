import pytest
import requests

from configuration import DOG_API_URL


@pytest.fixture()
def get_breeds():
    return requests.get(f"{DOG_API_URL}/breeds/list/all")


def request_by_breed(breed):
    return requests.get(f"{DOG_API_URL}/breed/{breed}/images")


def request_by_breed_rnd(breed, number):
    return requests.get(f"{DOG_API_URL}/breed/{breed}/images/random/{number}")


def request_sub_breeds(breed):
    return requests.get(f"{DOG_API_URL}/breed/{breed}/list")


@pytest.fixture()
def get_by_breed():
    return request_by_breed


@pytest.fixture()
def get_by_breed_rnd():
    return request_by_breed_rnd


@pytest.fixture()
def get_sub_breeds():
    return request_sub_breeds
