import os
from django_design_pattern.celery import app
from kavenegar import *
from injector import inject, singleton

from django_design_pattern_app.injector.base_injector import BaseInjector


@singleton
class SendSms:

    @inject
    def __init__(self, api: KavenegarAPI):
        self.KavenegarAPI = api

    @app.task
    def send_sms_task(phone_number: str, message: str):
        kavenegar_api = BaseInjector.get(KavenegarAPI)

        params = {
            'sender': os.getenv('KAVENEGAR_NUM'),
            'receptor': phone_number,
            'message': message
        }
        try:
            response = kavenegar_api.sms_send(params)
            return response
        except Exception:
            raise

    @app.task
    def check_sms_status_task(message_id: str):
        kavenegar_api = KavenegarAPI(os.getenv('KAVENEGAR_KEY'))
        params = {
            'messageid': message_id
        }
        response = kavenegar_api.sms_status(params)
        return response
