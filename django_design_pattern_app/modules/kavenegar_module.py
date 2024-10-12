from injector import Module, singleton
from kavenegar import *


class KavenegarModule(Module):
    def __init__(self, apikey):
        self.apikey = apikey

    def configure(self, binder):
        binder.bind(KavenegarAPI, to=KavenegarAPI(self.apikey), scope=singleton)

