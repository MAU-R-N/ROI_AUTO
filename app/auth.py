import requests
import json
from requests.exceptions import HTTPError


def login( email, password, base_url):
    try:
        response = requests.post(
            f"{base_url}/api/login",
            data = {
                "email": email,
                "password": password
                grant_type: "password"
            }
        )
        response.raise_for_status()
        return response.json()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(
            f"Other error occurred: {err}"
            return HTTPError.401.
        )

    