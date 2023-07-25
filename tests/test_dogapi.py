import pytest
import requests
import os


@pytest.mark.parametrize("url, status_code", [(os.getenv("url"), os.getenv("status_code"))])
def test_with_options(url, status_code):
    result = requests.get(url)

    assert result.status_code == int(status_code)
