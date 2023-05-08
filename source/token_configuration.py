from os import getenv
from dotenv import load_dotenv

load_dotenv()
FRESHDESK_TOKEN = getenv("FRESHDESK_TOKEN")
GITHUB_TOKEN = getenv("GITHUB_TOKEN")

if not FRESHDESK_TOKEN:
    raise Exception("No given Freshdesk token as environmental variable")

if not GITHUB_TOKEN:
    raise Exception("No given Github token as environmental variable")




