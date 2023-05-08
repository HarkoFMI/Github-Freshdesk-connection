import sys
import unittest

from source.helper_functions import github_user_info, create_payload, make_freshdesk_contact


class TestArgumentsParsing(unittest.TestCase):

    def test_invalid_number_of_arguments(self):
        with self.assertRaises(Exception):
            sys.argv = ['main.py', 'github_username']
            exec(open('main.py').read())

    def test_valid_number_of_arguments(self):
        sys.argv = ['main.py', 'username', 'domain']
        exec(open('main.py').read())


class TestGithubUserInfoFunction(unittest.TestCase):

    def test_github_user_info_success(self):
        result = github_user_info("HarkoFMI")

        self.assertEqual(result["name"], "Harut Partamian")
        self.assertEqual(result["bio"], None)
        self.assertEqual(result["type"], "User")
        self.assertEqual(result["email"], None)
        self.assertNotEqual(result["login"], "Jorko")


class TestCreatePayload(unittest.TestCase):

    def test_invalid_name(self):
        user_info = {"name": None}

        with self.assertRaises(Exception):
            create_payload(user_info)

    def test_invalid_email(self):
        user_info = {
            "email": None,
            "name": "Jorko"
        }

        with self.assertRaises(Exception):
            create_payload(user_info)


class TestFreshdeskContact(unittest.TestCase):

    def test_invalid_domain(self):
        user_info = {
            "email": "alabala@nica.com",
            "name": "Jorko"
        }
        invalid_domain = "alabalanica"

        with self.assertRaises(Exception):
            make_freshdesk_contact(user_info, invalid_domain)


if __name__ == "__main__":
    unittest.main()
