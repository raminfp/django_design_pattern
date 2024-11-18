from injector import Module, singleton
from kavenegar import *


class KavenegarModule(Module):
    def __init__(self, apikey):
        """
        Initialize the KavenegarModule with the API key.

        :param apikey: The API key for Kavenegar.
        """
        self.apikey = apikey

    def configure(self, binder):
        """
        Configure the KavenegarModule.

        This method is called when the module is installed. It is responsible
        for registering the KavenegarAPI with the injector.

        :param binder: The injector's binder.
        :type binder: injector.Binder
        """
        binder.bind(KavenegarAPI, to=KavenegarAPI(self.apikey), scope=singleton)

