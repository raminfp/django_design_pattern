import os
from django_design_pattern.celery import app
from kavenegar import *
from injector import inject, singleton

from django_design_pattern_app.injector.base_injector import BaseInjector


@singleton
class SendSms:

    @inject
    def __init__(self, api: KavenegarAPI):
        """
        Initialize the SendSms instance with the Kavenegar API.

        :param api: The Kavenegar API instance.
        """
        self.KavenegarAPI = api

    @app.task
    def send_sms_task(phone_number: str, message: str):
        """
        Send an SMS to the given phone number with the given message.

        :param phone_number: The phone number to send the SMS to.
        :param message: The message to be sent.

        :return: The response from the Kavenegar API.
        """
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
        """
        Check the status of an SMS message.

        :param message_id: The message_id returned by sms_send method.
        :return: The response from the Kavenegar API.
        """
        kavenegar_api = KavenegarAPI(os.getenv('KAVENEGAR_KEY'))
        params = {
            'messageid': message_id
        }
        response = kavenegar_api.sms_status(params)
        return response
