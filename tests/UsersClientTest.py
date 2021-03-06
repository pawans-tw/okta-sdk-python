import unittest
import os
import json

from okta import UsersClient
from okta.models.user import User

config_path = os.path.normpath(os.path.join(os.path.dirname(__file__),
                                            '../.sdk.config.json'))

with open(config_path) as sdk_config_data:
    sdk_config = json.load(sdk_config_data)


def build_client(test_description):
    url = '{}:{}'.format(sdk_config['mockOkta']['proxy'],
                         sdk_config['mockOkta']['port'])
    return UsersClient(
        base_url=url,
        api_token=sdk_config['mockOkta']['apiKey'],
        headers={
            'x-test-description': test_description
        }
    )


class UsersClientTest(unittest.TestCase):

    def tests_client_initializer_args(self):
        client = UsersClient('https://example.okta.com', 'api_key')

    def tests_client_initializer_kwargs(self):
        client = UsersClient(base_url='https://example.okta.com', api_token='api_key')

    def test_requests_a_user(self):
        client = build_client('/api/v1/users/:id - requests a user')
        users = client.get_users()
        client.get_user(users[0].id)

    def test_creates_a_user_without_credentials(self):
        client = build_client('/api/v1/users/:id - creates a user without credentials')
        user = User(login='mocktestexample-brutis@mocktestexample.com',
                    email='mocktestexample-brutis@mocktestexample.com',
                    firstName='First',
                    lastName='McJanky',
                    secondEmail='asdrg@example.com',
                    employeeNumber='1',
                    mobile_phone='some mobile number',
                    telephone='some telephone number',
                    country='some country',
                    homeOffice='some home office',
                    workingOffice='some working office',
                    department='some department',
                    departmentCode='some department code',
                    role='some role',
                    joinDate='some date'
        )
        client.create_user(user)

    def test_creates_a_user_in_a_group(self):
        client = build_client('/api/v1/users/:id - creates a user without credentials')
        user = User(login='mocktestexample-brutis@mocktestexample.com',
                    email='mocktestexample-brutis@mocktestexample.com',
                    firstName='First',
                    lastName='McJanky',
                    secondEmail='asdrg@example.com',
                    employeeNumber='1',
                    mobile_phone='some mobile number',
                    telephone='some telephone number',
                    country='some country',
                    homeOffice='some home office',
                    workingOffice='some working office',
                    department='some department',
                    departmentCode='some department code',
                    role='some role',
                    joinDate='some date',
                    groupIds=['some group id']
        )
        client.create_user(user)

    def test_update_a_user(self):
        client = build_client('/api/v1/users/:id - updates a user')
        user = client.get_user('mocktestexample-frutis@mocktestexample.com')
        user.profile.firstName = 'NewFirst'

        # Format request to satisfy yakback
        user_profile = {
            'profile': user.profile
        }
        client.update_user_by_id(user.id, user_profile)

    def test_delete_a_user(self):
        client = build_client('/api/v1/users/:id - deletes a user')
        user = client.get_user('mocktestexample-deleteme@mocktestexample.com')
        client.delete_user(user.id)

    def test_get_user_groups(self):
        client = build_client('/api/v1/users/:id - get user groups')
        user = client.get_user('mocktestexample-fruitis@mocktestexample.com')
        client.get_user_groups(user.id)

    def test_activate_user(self):
        client = build_client('/api/v1/users/:id/lifecycle - activates a user')
        user = client.get_user('mocktestexample-deactive@mocktestexample.com')
        client.activate_user(user.id)

    def test_deactivate_user(self):
        client = build_client('/api/v1/users/:id/lifecycle - deactivates a user')
        user = client.get_user('mocktestexample-deactive@mocktestexample.com')
        client.deactivate_user(user.id)

    def test_change_password(self):
        client = build_client('/api/v1/users/:id/credentials - change a user password')
        user = client.get_user('mocktestexample-frutis@mocktestexample.com')
        client.change_password(user.id, 'Asdf1234', 'Asdf1234!')

    def test_reset_password(self):
        client = build_client('/api/v1/users/:id/lifecycle - reset a user password')
        user = client.get_user('mocktestexample-frutis@mocktestexample.com')
        client.reset_password(user.id, False)

    def test_expire_password(self):
        client = build_client('/api/v1/users/:id/credentials - expires a user password')
        user = client.get_user('mocktestexample-frutis@mocktestexample.com')
        client.expire_password(user.id)
