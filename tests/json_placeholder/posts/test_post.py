import pytest

from src.baseclasses.baseresponse import BaseResponse
from src.pydantic_schemas.json_placeholder.post import Post


class TestPost:

    @pytest.mark.parametrize("post_id", [1, 50, 70, 100])
    def test_get_post_by_id(self, post_id, get_post_by_id):
        BaseResponse(get_post_by_id(post_id)).assert_status_code(200).validate(Post)

    @pytest.mark.parametrize("post_id", [-1, 0, 101])
    def test_get_post_by_invalid_id(self, post_id, get_post_by_id):
        response = BaseResponse(get_post_by_id(post_id)).assert_status_code(404)

        assert response.response_json == {}

    @pytest.mark.parametrize("user_id", [1, 5, 10])
    def test_filter_posts_by_userid(self, user_id, filter_posts_by_userid):
        BaseResponse(filter_posts_by_userid(user_id)).assert_status_code(200).validate(Post)

    @pytest.mark.parametrize("user_id", [-1, 0, 11])
    def test_filter_posts_by_invalid_userid(self, user_id, filter_posts_by_userid):
        response = BaseResponse(filter_posts_by_userid(user_id)).assert_status_code(200)

        assert response.response_json == []

    def test_get_posts(self, get_posts):
        BaseResponse(get_posts).assert_status_code(200).validate(Post)

    @pytest.mark.parametrize("create_post_data", [
        {"title": "Post title5", "body": "This is a post5", "userId": 5},
        {"title": "Post title1", "body": "This is a post1", "userId": 1},
        {"title": "Post title10", "body": "This is a post10", "userId": 10},
    ], indirect=True)
    def test_create_post(self, create_post_request, get_post_by_id):
        """
        Important: resource will not be really updated on the server but it will be faked as if.
        BaseResponse(get_post_by_id(response.response_json.get("id"))).assert_status_code(200).validate(Post)
        """
        BaseResponse(create_post_request).assert_status_code(201).validate(Post)

    @pytest.mark.parametrize("update_post_data", [
        {"id": 1, "title": "Post title5", "body": "This is a post5", "userId": 5},
        {"id": 50, "title": "Post title1", "body": "This is a post1", "userId": 1},
        {"id": 100, "title": "Post title10", "body": "This is a post10", "userId": 10},
    ], indirect=True)
    def test_update_post(self, update_post_request):
        """Important: resource will not be really updated on the server but it will be faked as if."""
        BaseResponse(update_post_request).assert_status_code(200).validate(Post)

    @pytest.mark.parametrize("delete_post_request", [1, 50, 100], indirect=True)
    def test_delete_post(self, delete_post_request):
        response = BaseResponse(delete_post_request).assert_status_code(200)

        assert response.response_json == {}
