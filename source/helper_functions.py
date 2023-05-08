from pprint import pprint
from token_configuration import GITHUB_TOKEN
from requests import get


def github_user_info(username: str):
    url = f"https://api.github.com/users/{username}"
    response = get(url, auth=(f"{username}", f"{GITHUB_TOKEN}"))

    if response.status_code != 200:
        raise Exception(f"Error while getting information from Github API")

    return response.json()


pprint(github_user_info("HarkoFMI"))
