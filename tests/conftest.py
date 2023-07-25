import pytest
import os


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru", help="URL address")
    parser.addoption("--status_code", default="200", help="Expected HTTP response status code")


def pytest_configure(config):
    os.environ["url"] = config.getoption("--url")
    os.environ["status_code"] = config.getoption("--status_code")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
