from pydantic import BaseModel


class SubBreeds(BaseModel):
    message: list[str]
    status: str
