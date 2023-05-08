from pprint import pprint

import requests

from token_configuration import GITHUB_TOKEN, FRESHDESK_TOKEN


def github_user_info(username: str):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=(f"{username}", f"{GITHUB_TOKEN}"))

    if response.status_code != 200:
        raise Exception(f"Error while getting information from Github API")

    return response.json()


pprint(github_user_info("HarkoFMI"))


def create_payload(user_info):
    payload = {}

    if user_info["name"]:
        payload["name"] = user_info["name"]
    else:
        raise Exception("Cannot create contact without name!")

    if user_info["email"]:
        payload["email"] = user_info["email"]
    if user_info["location"]:
        payload["address"] = user_info["location"]
    if user_info["bio"]:
        payload["description"] = user_info["bio"]

    return payload


pprint(create_payload(github_user_info("HarkoFMI")))



