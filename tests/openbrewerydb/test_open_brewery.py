import pytest

from src.baseclasses.baseresponse import BaseResponse
from src.pydantic_schemas.openbrewery_api.brewery import Brewery

from src.enums.openbrewery_api.brewery_type import BreweryType
from src.utils.brewery_utils import get_test_data, inject_test_data_ids


class TestOpenBrewery:
    test_data = get_test_data(count=20)
    test_data_ids = inject_test_data_ids(count=20)

    @pytest.mark.parametrize("id_", test_data["brewery_ids"])
    def test_single_brewery(self, id_, get_single_brewery):
        result = BaseResponse(get_single_brewery(id_)).assert_status_code(200).validate(Brewery)
        assert result.response_json.get("id") == id_

    @pytest.mark.parametrize("id_, exp_name",
                             [
                                 ("b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0", "MadTree Brewing 2.0"),
                                 ("5128df48-79fc-4f0f-8b52-d06be54d0cec", "(405) Brewing Co"),
                                 ("9c5a66c8-cc13-416f-a5d9-0a769c87d318", "(512) Brewing Co"),
                                 ("ef970757-fe42-416f-931d-722451f1f59c", "10 Barrel Brewing Co"),
                                 ("6d14b220-8926-4521-8d19-b98a2d6ec3db", "10 Barrel Brewing Co"),
                                 ("e2e78bd8-80ff-4a61-a65c-3bfbd9d76ce2", "10 Barrel Brewing Co"),
                                 ("9f1852da-c312-42da-9a31-097bac81c4c0", "10 Barrel Brewing Co - Bend Pub"),
                             ])
    def test_single_brewery_name_by_id(self, id_, exp_name, get_single_brewery):
        result = BaseResponse(get_single_brewery(id_)).assert_status_code(200).validate(Brewery)
        assert result.response_json.get("name") == exp_name

    @pytest.mark.parametrize("ids", [brewery_id for brewery_id in test_data["brewery_ids"]])
    def test_brewery_by_ids(self, ids, get_brewery_by_ids):
        BaseResponse(get_brewery_by_ids(ids)).assert_status_code(200).validate(Brewery)

    @pytest.mark.parametrize("ids", test_data_ids, ids=",".join)
    def test_brewery_by_ids_commas(self, ids, get_brewery_by_ids):
        BaseResponse(get_brewery_by_ids(",".join(ids))).assert_status_code(200).validate(Brewery)

    @pytest.mark.parametrize("brewery_type", [*BreweryType.list()])
    def test_brewery_by_type(self, brewery_type, get_brewery_by_type):
        BaseResponse(get_brewery_by_type(brewery_type)).assert_status_code(200).validate(Brewery)
