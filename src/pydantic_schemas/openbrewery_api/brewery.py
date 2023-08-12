from pydantic import BaseModel
from pydantic import HttpUrl, UUID4
from typing import Optional
from src.enums.openbrewery_api.brewery_type import BreweryType


class Brewery(BaseModel):
    id: UUID4
    name: str
    brewery_type: BreweryType
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: Optional[float]
    latitude: Optional[float]
    phone: Optional[str]
    website_url: Optional[HttpUrl]
    state: str
    street: Optional[str]
