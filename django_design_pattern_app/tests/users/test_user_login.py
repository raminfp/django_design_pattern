from rest_framework.test import APIClient
from django_design_pattern_app.tests import base_test


class UserLoginTestCase(base_test.NewUserTestCase):
    """
    This class is used to test the login functionality and
    check whether a user is successfully getting logged in to the
    system.
    """

    def setUp(self) -> None:
        super().setUp()

    def test_user_login(self):
        client = APIClient()
        result = client.post('/api/v1/auth', {'mobile': "09191583239"},
                             format='json')
        self.assertEquals(result.status_code, 200)

    def tearDown(self) -> None:
        self.client.logout()
        super().tearDown()


class LoginTokenVerifyTestCase(base_test.NewUserTestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_user_login_token_verify(self):
        client = APIClient()
        login_response = client.post('/api/v1/verify', {
                                                            'code': "123456",
                                                             'password': "09191583239"
                                                        },
                                     format='json')

        token_verify_response = client.post('/api/v1/user/token-verify/',
                                            {'token': login_response.json()['access']},
                                            format='json')

        self.assertEquals(token_verify_response.status_code, 200)

    def tearDown(self) -> None:
        self.client.logout()
#         super().tearDown()