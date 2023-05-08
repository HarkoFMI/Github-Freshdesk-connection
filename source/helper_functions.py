import requests
from pprint import pprint
from source.token_configuration import GITHUB_TOKEN, FRESHDESK_TOKEN


def github_user_info(username: str):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=(username, GITHUB_TOKEN))

    if response.status_code != 200:
        raise Exception(f"Error while getting information from Github API")

    return response.json()


# pprint(github_user_info("HarkoFMI"))


def create_payload(user_info):
    payload = {}

    if user_info["name"]:
        payload["name"] = user_info["name"]
    else:
        raise Exception("Cannot create contact without name!")

    if user_info["email"]:
        payload["email"] = user_info["email"]
    else:
        raise Exception("Cannot create contact without email!")
    if user_info["location"]:
        payload["address"] = user_info["location"]
    if user_info["bio"]:
        payload["description"] = user_info["bio"]

    return payload


# pprint(create_payload(github_user_info("HarkoFMI")))


def make_freshdesk_contact(user_info, domain: str):
    payload = create_payload(user_info)

    url = f"https://{domain}.freshdesk.com/api/v2/contacts"
    response = requests.get(url, auth=(FRESHDESK_TOKEN, "X"))
    for contact in response.json():
        if contact["name"] == user_info["name"]:
            request = requests.put(f'https://{domain}.freshdesk.com/api/v2/contacts/{contact["id"]}', json=payload,
                                   auth=(FRESHDESK_TOKEN, "X"))

            if 199 < request.status_code < 300:
                raise Exception(
                    "Error with updating the freshdesk contact with query status code: {request.status_code}")

            return "Updated contact successfully"

    request = requests.post(f'https://{domain}.freshdesk.com/api/v2/contacts', json=payload,
                            auth=(FRESHDESK_TOKEN, "X"))
    if not 199 < request.status_code < 300:
        raise Exception(f"Error with creating the freshdesk contact with query status code: {request.status_code}")

    return "Created contact successfully"

# print(make_freshdesk_contact("HarkoFMI", "harutpartamian"))
