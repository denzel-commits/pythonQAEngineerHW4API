import requests
import time
from src.baseclasses.baseresponse import BaseResponse


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url

    def _request(self, url, request_type, json=None, expected_error=False):
        stop_flag = False
        max_retries = 3
        attempt = 0
        retry_delay_secs = 3

        while not stop_flag:
            attempt += 1

            if request_type == "GET":
                response = requests.get(url)
            elif request_type == "POST":
                response = requests.post(url, json=json)
            elif request_type == "PUT":
                response = requests.put(url, json=json)
            elif request_type == "PATCH":
                response = requests.patch(url, json=json)
            elif request_type == "DELETE":
                response = requests.delete(url)

            if not expected_error and response.ok:
                stop_flag = True
            elif expected_error:
                stop_flag = True
            elif attempt >= max_retries:
                stop_flag = True

            if not stop_flag:
                time.sleep(retry_delay_secs)

        return BaseResponse(response)

    def get(self, endpoint, endpoint_id=None, expected_error=False):
        if endpoint_id is None:
            url = f"{self.base_url}/{endpoint}"
        else:
            url = f"{self.base_url}/{endpoint}/{endpoint_id}"

        return self._request(url, "GET", expected_error=expected_error)

    def post(self, endpoint, body, endpoint_id=""):
        url = f"{self.base_url}/{endpoint}/{endpoint_id}"
        return self._request(url, "POST", json=body)

    def put(self, endpoint, body, endpoint_id=""):
        url = f"{self.base_url}/{endpoint}/{endpoint_id}"
        return self._request(url, "PUT", json=body)

    def patch(self, endpoint, body, endpoint_id=""):
        url = f"{self.base_url}/{endpoint}/{endpoint_id}"
        return self._request(url, "PATCH", json=body)

    def delete(self, endpoint, endpoint_id):
        url = f"{self.base_url}/{endpoint}/{endpoint_id}"
        return self._request(url, "DELETE")
