from source.arguments_parsing import github_username, freshdesk_domain
from source.database import create_table, insert_user, close_db
from source.helper_functions import github_user_info, make_freshdesk_contact


if __name__ == "__main__":
    user_info = github_user_info(github_username)

    create_table()
    insert_user(user_info["login"], user_info["name"], user_info["created_at"])
    close_db()

    make_freshdesk_contact(user_info, freshdesk_domain)


