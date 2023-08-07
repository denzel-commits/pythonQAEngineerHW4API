import requests
import pytest
from configuration import JSON_PLACEHOLDER_API_URL
from src.baseclasses.baserequest import BaseRequest


def post_by_id(id_, expected_error=False):
    return BaseRequest(JSON_PLACEHOLDER_API_URL).get("posts", id_, expected_error=expected_error)


def filter_by_userid(userid):
    return BaseRequest(JSON_PLACEHOLDER_API_URL).get(f"posts?userId={userid}")


@pytest.fixture()
def get_posts():
    return BaseRequest(JSON_PLACEHOLDER_API_URL).get("posts")


@pytest.fixture()
def get_post_by_id():
    return post_by_id


@pytest.fixture()
def filter_posts_by_userid():
    return filter_by_userid


@pytest.fixture()
def create_post_data(request):
    post_data = request.param
    return {"title": post_data["title"],
            "body": post_data["body"],
            "userId": post_data["userId"],
            }


@pytest.fixture()
def create_post_request(create_post_data):
    return BaseRequest(JSON_PLACEHOLDER_API_URL).post("posts", body=create_post_data)


@pytest.fixture()
def update_post_data(request):
    post_data = request.param
    return {"id": post_data["id"],
            "title": post_data["title"],
            "body": post_data["body"],
            "userId": post_data["userId"],
            }


@pytest.fixture()
def update_post_request(update_post_data):
    return BaseRequest(JSON_PLACEHOLDER_API_URL).put("posts", endpoint_id=update_post_data['id'], body=update_post_data)


@pytest.fixture()
def delete_post_request(request):
    return BaseRequest(JSON_PLACEHOLDER_API_URL).delete("posts", endpoint_id=request.param)
