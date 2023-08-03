import requests


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url

    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        while not stop_flag:
            if request_type == "GET":
                response = requests.get(url)
            elif request_type == "POST":
                response = requests.post(url, data=data)
            else:
                response = requests.delete(url)

            if not expected_error and response.ok:
                stop_flag = True
            elif expected_error:
                stop_flag = True

        return response

    def get(self, endpoint, endpoint_id, expected_error):
        url = f"{self.base_url}/{endpoint}/{endpoint_id}"
        response = self._request(url, "GET", expected_error=expected_error)
        return response.json()

    def post(self, endpoint, endpoint_id, body):
        url = f"{self.base_url}/{endpoint}/{endpoint_id}"
        response = self._request(url, "POST", data=body)
        return response.json()["message"]

    def delete(self, endpoint, endpoint_id):
        url = f"{self.base_url}/{endpoint}/{endpoint_id}"
        response = self._request(url, "DELETE")
        return response.json()["message"]
