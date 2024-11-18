from django_design_pattern_app.repositories.base_repo import BaseRepo
from django_design_pattern_app.schemas.users import RegisterUserSchema
from django_design_pattern_app.services.sms.tasks import SendSms
from django_design_pattern_app.models.users import Users
from typing import List, Optional
from django.db.transaction import atomic


class UsersRepo(BaseRepo):

    # TODO : Change all methods here to something you can use
    # Elastic Search
    def elk_search(self):
        """
        Search all users in Elastic Search.

        Returns:
            dict: Aggregations of users.
        """
        query = {}
        aggs = {}
        data = self.elk.new_search(query=query, aggs=aggs, size=0)
        return data

    def minio_find(self):
        """
        Find an object in MinIO.

        Currently, this method always returns an empty string.

        Returns:
            str: The object name.
        """
        return self.service_minio.find_object("", "")

    @staticmethod
    def log_sms(phone_number: str, message: str):
        """
        Send a log SMS to the given phone number with the given message.

        Args:
            phone_number (str): The phone number to send the SMS to.
            message (str): The message to be sent.

        Returns:
            None
        """
        SendSms().send_sms_task.delay(phone_number, message)


    @atomic
    def get_users(self) -> List[Users]:
        """
        Get all users in the database.

        Returns:
            List[Users]: A list of all users in the database.
        """
        return list(Users.objects.all())

    @atomic
    def get_user_by_phone(self, phone: str) -> Optional[Users]:
        """
        Retrieves a user by phone number.

        Args:
            phone (str): The phone number to search for.

        Returns:
            Optional[Users]: The user with the given phone number or None if no user is found.
        """
        user_filter = Users.objects.filter(phone=phone)

        if user_filter:
            return user_filter.first()
        return None

    @atomic
    def get_user_by_id(self, user_id: int) -> Optional[Users]:
        """
        Retrieves a user by ID.

        Args:
            user_id (int): The ID of the user to search for.

        Returns:
            Optional[Users]: The user with the given ID or None if no user is found.
        """
        return Users.objects.get(id=user_id)

    @atomic
    def check_new_user(self, phone_number: str) -> bool:
        """
        Checks if the user with the given phone number is new or not.

        Args:
            phone_number (str): The phone number to check.

        Returns:
            bool: True if the user is not new, False otherwise.
        """
        return Users.objects.filter(phone=phone_number, is_new_user=False).exists()

    @atomic
    def update_user(self, user_id: int, data: RegisterUserSchema) -> Optional[Users]:
        # Retrieve the user by ID
        """
        Updates the user with the given ID with the new data.

        Args:
            user_id (int): The ID of the user to update.
            data (RegisterUserSchema): The new data to update the user with.

        Returns:
            Optional[Users]: The updated user instance if the user with the given ID exists, None otherwise.
        """
        user = self.get_user_by_id(user_id)
        if user:
            # Update the user's fields with the new data
            for attr, value in data.dict().items():
                setattr(user, attr, value)
            # Save the updated user instance
            user.save()
            return user
        return None

    @atomic
    def get_total_user(self):
        """
        Retrieves the total number of users.

        Returns:
            int: The total number of users.
        """
        return Users.objects.count()
