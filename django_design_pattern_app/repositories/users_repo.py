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
        query = {}
        aggs = {}
        data = self.elk.new_search(query=query, aggs=aggs, size=0)
        return data
    # MinIO
    def minio_find(self):
        return self.service_minio.find_object("", "")

    # SMS Service
    @staticmethod
    def log_sms(phone_number: str, message: str):
        SendSms().send_sms_task.delay(phone_number, message)

    # ORM postgresql
    @atomic
    def get_users(self) -> List[Users]:
        return list(Users.objects.all())

    @atomic
    def get_user_by_phone(self, phone: str) -> Optional[Users]:
        user_filter = Users.objects.filter(phone=phone)

        if user_filter:
            return user_filter.first()
        return None

    @atomic
    def get_user_by_id(self, user_id: int) -> Optional[Users]:
        return Users.objects.get(id=user_id)

    @atomic
    def check_new_user(self, phone_number: str) -> bool:
        return Users.objects.filter(phone=phone_number, is_new_user=False).exists()

    @atomic
    def update_user(self, user_id: int, data: RegisterUserSchema) -> Optional[Users]:
        # Retrieve the user by ID
        user = self.get_user_by_id(user_id)
        if user:
            # Update the user's fields with the new data
            for attr, value in data.dict().items():
                setattr(user, attr, value)
            # Save the updated user instance
            user.save()
            return user

    @atomic
    def get_total_user(self):
        return Users.objects.count()