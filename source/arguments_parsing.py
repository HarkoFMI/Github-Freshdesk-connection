import sys

if len(sys.argv) != 3:
    raise Exception("Please use the script with 2 arguments - Github username and Freshdesk domain name")

github_username = sys.argv[1]
freshdesk_domain = sys.argv[2]
