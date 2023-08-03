import requests
from configuration import OPEN_BREWERY_API_URL


def get_test_data(count=10):
    params = {"per_page": count}
    response = requests.get(f"{OPEN_BREWERY_API_URL}/breweries", params=params)

    return {"brewery_ids": [item["id"] for item in response.json()],
            "brewery_cities": [item["city"] for item in response.json()],
            "brewery_names": [item["name"] for item in response.json()]
            }


def inject_test_data_ids(count=10):
    test_data = get_test_data(count)
    return [(test_data["brewery_ids"][i], test_data["brewery_ids"][i + 1])
            for i in range(0, len(test_data["brewery_ids"]), 2)
            ]
