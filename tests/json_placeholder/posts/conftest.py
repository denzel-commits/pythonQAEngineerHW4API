import requests
import pytest
from configuration import JSON_PLACEHOLDER_API_URL


def post_by_id(id_):
    return requests.get(JSON_PLACEHOLDER_API_URL + f"/posts/{id_}")


def filter_by_userid(userid):
    return requests.get(JSON_PLACEHOLDER_API_URL + f"/posts?userId={userid}")


@pytest.fixture()
def get_posts():
    return requests.get(JSON_PLACEHOLDER_API_URL + "/posts")


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
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    return requests.post(JSON_PLACEHOLDER_API_URL + "/posts", json=create_post_data, headers=headers)


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
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    return requests.put(JSON_PLACEHOLDER_API_URL + f"/posts/{update_post_data['id']}", json=update_post_data,
                        headers=headers)


@pytest.fixture()
def delete_post_request(request):
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    return requests.delete(JSON_PLACEHOLDER_API_URL + f"/posts/{request.param}", headers=headers)
