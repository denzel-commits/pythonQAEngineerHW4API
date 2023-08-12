import pytest

from src.baseclasses.baseresponse import BaseResponse
from src.pydantic_schemas.dogs_api.breeds import Breeds
from src.pydantic_schemas.dogs_api.images import Images
from src.pydantic_schemas.dogs_api.subbreeds import SubBreeds


class TestDogApi:
    @pytest.mark.parametrize("status", ["success"])
    def test_list_breeds(self, get_breeds, status):
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
    def test_by_breed(self, breed, status, get_by_breed):
        result = BaseResponse(get_by_breed(breed))\
            .assert_status_code(200) \
            .validate(Images)

        assert result.response_json["status"] == status

    @pytest.mark.parametrize("breed, number, image_ext, status", [
                                 ("hound", 3, ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'), "success"),
                                 ("bulldog", 1, ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'), "success"),
                                 ("cattledog", 4, ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'), "success"),
                                 ("corgi", 10, ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'), "success"),
                             ])
    def test_by_breed_rnd(self, breed, number, image_ext, status, get_by_breed_rnd):
        result = BaseResponse(get_by_breed_rnd(breed, number))\
            .assert_status_code(200) \
            .validate(Images)

        assert result.response_json["status"] == status

        for image in result.response_json["message"]:
            assert image.lower().endswith(image_ext)

    @pytest.mark.parametrize("breed, sub_breeds, status", [
        ("hound", ["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"], "success"),
        ("bulldog", ["boston", "english", "french"], "success"),
        ("cattledog", ["australian"], "success"),
        ("corgi", ["cardigan"], "success"),
    ])
    def test_list_sub_breeds(self, status, breed, sub_breeds, get_sub_breeds):
        result = BaseResponse(get_sub_breeds(breed))\
            .assert_status_code(200) \
            .validate(SubBreeds)

        assert result.response_json["status"] == status

        assert result.response_json["message"] == sub_breeds

    @pytest.mark.parametrize("breed, status", [
        ("honda", "error"),
        ("bullbuzzer", "error"),
        ("cattle2", "error"),
        ("corgin", "error"),
    ])
    def test_list_sub_breeds_invalid(self, status, breed, get_sub_breeds):
        result = BaseResponse(get_sub_breeds(breed)).assert_status_code(404)

        assert result.response_json["status"] == status

        assert result.response_json["message"] == "Breed not found (master breed does not exist)"

    @pytest.mark.parametrize("breed, subbreed, number, image_ext, status", [
        ("hound", "afghan", 3, ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'), "success"),
        ("bulldog", "french", 1, ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'), "success"),
        ("cattledog", "australian", 4, ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'), "success"),
        ("corgi", "cardigan", 10, ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'), "success"),
    ])
    def test_sub_breeds_rnd(self, breed, subbreed, number, image_ext, status, get_sub_breeds_rnd):
        result = BaseResponse(get_sub_breeds_rnd(breed, subbreed, number))\
            .assert_status_code(200) \
            .validate(Images)

        assert result.response_json["status"] == status

        for image in result.response_json["message"]:
            assert image.lower().endswith(image_ext)
