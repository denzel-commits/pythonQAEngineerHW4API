import pytest

from src.baseclasses.baseresponse import BaseResponse
from src.pydantic_schemas.dogs_api.breeds import Breeds
from src.pydantic_schemas.dogs_api.images import Images
from src.pydantic_schemas.dogs_api.subbreeds import SubBreeds


@pytest.mark.parametrize("status", ["success"])
def test_list_breeds(get_breeds, status):
    result = BaseResponse(get_breeds)\
        .assert_status_code(200) \
        .validate(Breeds)

    assert result.response_json["status"] == status


@pytest.mark.parametrize("breed, status", [
    ("hound", "success"),
    ("bulldog", "success"),
    ("cattledog", "success"),
    ("corgi", "success"),
])
def test_by_breed(breed, status, get_by_breed):
    result = BaseResponse(get_by_breed(breed))\
        .assert_status_code(200) \
        .validate(Images)

    assert result.response_json["status"] == status


@pytest.mark.parametrize("breed, number, status", [
                             ("hound", 3, "success"),
                             ("bulldog", 1, "success"),
                             ("cattledog", 4, "success"),
                             ("corgi", 10, "success"),
                         ])
def test_by_breed_rnd(breed, number, status, get_by_breed_rnd):
    result = BaseResponse(get_by_breed_rnd(breed, number))\
        .assert_status_code(200) \
        .validate(Images)

    assert result.response_json["status"] == status


@pytest.mark.parametrize("breed, status", [
    ("hound", "success"),
    ("bulldog", "success"),
    ("cattledog", "success"),
    ("corgi", "success"),
])
def test_list_sub_breeds(status, breed, get_sub_breeds):
    result = BaseResponse(get_sub_breeds(breed))\
        .assert_status_code(200) \
        .validate(SubBreeds)

    assert result.response_json["status"] == status


@pytest.mark.parametrize("breed, subbreed, number, status", [
    ("hound", "afghan", 3, "success"),
    ("bulldog", "french", 1, "success"),
    ("cattledog", "australian", 4, "success"),
    ("corgi", "cardigan", 10, "success"),
])
def test_sub_breeds_rnd(breed, subbreed, number, status, get_sub_breeds_rnd):
    result = BaseResponse(get_sub_breeds_rnd(breed, subbreed, number))\
        .assert_status_code(200) \
        .validate(Images)

    assert result.response_json["status"] == status
    