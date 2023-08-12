import pytest
import requests
import os


@pytest.mark.parametrize("url, status_code", [(os.getenv("url"), os.getenv("status_code"))])
def test_url_status(url, status_code):
    response = requests.get(url)

    assert response.status_code == int(status_code)
