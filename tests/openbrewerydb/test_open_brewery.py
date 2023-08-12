import pytest

from src.baseclasses.baseresponse import BaseResponse
from src.enums.openbrewery_api.brewery_type import BreweryType
from src.pydantic_schemas.openbrewery_api.brewery import Brewery
from src.utils.brewery_utils import get_test_data, inject_test_data_ids, inject_test_data_id_name


class TestOpenBrewery:
    test_data = get_test_data(count=20)
    test_data_ids = inject_test_data_ids(count=20)
    test_data_id_name = inject_test_data_id_name("openbrewery_id_name.csv")

    @pytest.mark.parametrize("id_", test_data["brewery_ids"])
    def test_single_brewery(self, id_, get_single_brewery):
        result = BaseResponse(get_single_brewery(id_)).assert_status_code(200).validate(Brewery)
        assert result.response_json.get("id") == id_

    @pytest.mark.parametrize("id_, exp_name", test_data_id_name)
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
        breweries = BaseResponse(get_brewery_by_type(brewery_type)).assert_status_code(200).validate(Brewery)

        if isinstance(breweries.response_json, list):
            for brewery in breweries.response_json:
                assert brewery.get("brewery_type") == brewery_type
        else:
            assert breweries.get("brewery_type") == brewery_type

    @pytest.mark.parametrize("brewery_type", ["macro", "mini"])
    def test_brewery_by_type_invalid(self, brewery_type, get_brewery_by_type):
        result = BaseResponse(get_brewery_by_type(brewery_type)).assert_status_code(400)
        assert "errors" in result.response_json
        assert result.response_json == {'errors': ['Brewery type must include one of these types: '
                                                   '["micro", "nano", "regional", "brewpub", "large", '
                                                   '"planning", "bar", "contract", "proprietor", "closed"]']}
