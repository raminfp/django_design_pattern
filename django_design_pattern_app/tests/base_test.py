import datetime

from django.test import TestCase
from ngr_diag_isaco_app.models import Users
from faker import Faker


class NewUserTestCase(TestCase):
    """
    This class is going to be inherited by other sub-classes.
    """


    def setUp(self) -> None:
        self.mobile = "09191583239"
        self.otp_code = "123456"
        self.user = Users.objects.create_user(mobile=self.mobile,
                                                    otp_code=self.otp_code,
                                                    update_otp=datetime.datetime.now()
                                                    )

    def tearDown(self) -> None:
        self.user.delete()
