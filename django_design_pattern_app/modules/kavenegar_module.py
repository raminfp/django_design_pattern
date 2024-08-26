from injector import Module, singleton
from django_design_pattern_app.services.sms.kavenegar import KavenegarAPI


class KavenegarModule(Module):
    def __init__(self, apikey):
        self.apikey = apikey

    def configure(self, binder):
        binder.bind(KavenegarAPI, to=KavenegarAPI(self.apikey), scope=singleton)

