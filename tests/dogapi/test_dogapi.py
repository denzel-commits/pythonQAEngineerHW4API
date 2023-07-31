import pytest

from src.baseclasses.baseresponse import BaseResponse
from src.pydantic_schemas.breeds import Breeds
from src.pydantic_schemas.images import Images
from src.pydantic_schemas.subbreeds import SubBreeds


@pytest.mark.parametrize("schema, status_code, status", [(Breeds, 200, "success")])
def test_list_breeds(get_breeds, schema, status_code, status):
    result = BaseResponse(get_breeds)\
        .assert_status_code(status_code) \
        .validate(schema)

    assert result.response_json["status"] == status


@pytest.mark.parametrize("schema, status_code, status, breed", [
    (Images, 200, "success", "hound"),
    (Images, 200, "success", "bulldog"),
    (Images, 200, "success", "cattledog"),
    (Images, 200, "success", "corgi"),
])
def test_by_breed(get_by_breed, schema, status_code, status, breed):
    result = BaseResponse(get_by_breed(breed))\
        .assert_status_code(status_code) \
        .validate(schema)

    assert result.response_json["status"] == status


@pytest.mark.parametrize("schema, status_code, status, breed, number", [
    (Images, 200, "success", "hound", 3),
    (Images, 200, "success", "bulldog", 1),
    (Images, 200, "success", "cattledog", 4),
    (Images, 200, "success", "corgi", 10),
])
def test_by_breed_rnd(get_by_breed_rnd, schema, status_code, status, breed, number):
    result = BaseResponse(get_by_breed_rnd(breed, number))\
        .assert_status_code(status_code) \
        .validate(schema)

    assert result.response_json["status"] == status


@pytest.mark.parametrize("schema, status_code, status, breed", [
    (SubBreeds, 200, "success", "hound"),
    (SubBreeds, 200, "success", "bulldog"),
    (SubBreeds, 200, "success", "cattledog"),
    (SubBreeds, 200, "success", "corgi"),
])
def test_list_sub_breeds(get_sub_breeds, schema, status_code, status, breed):
    result = BaseResponse(get_sub_breeds(breed))\
        .assert_status_code(status_code) \
        .validate(schema)

    assert result.response_json["status"] == status


@pytest.mark.parametrize("schema, status_code, status, breed, subbreed, number", [
    (Images, 200, "success", "hound", "afghan", 3),
    (Images, 200, "success", "bulldog", "french", 1),
    (Images, 200, "success", "cattledog", "australian", 4),
    (Images, 200, "success", "corgi", "cardigan", 10),
])
def test_sub_breeds_rnd(get_sub_breeds_rnd, schema, status_code, status, breed, subbreed, number):
    result = BaseResponse(get_sub_breeds_rnd(breed, subbreed, number))\
        .assert_status_code(status_code) \
        .validate(schema)

    assert result.response_json["status"] == status