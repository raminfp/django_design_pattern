import requests
import json


# Default requests timeout in seconds.
DEFAULT_TIMEOUT = 10


class KavenegarAPI(object):
    def __init__(self, apikey, timeout=None):
        self.version = 'v1'
        self.host = 'api.kavenegar.com'
        self.apikey = apikey
        self.timeout = timeout or DEFAULT_TIMEOUT
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'charset': 'utf-8'
        }

    def __repr__(self):
        return "kavenegar.KavenegarAPI({!r})".format(self.apikey)

    def __str__(self):
        return "kavenegar.KavenegarAPI({!s})".format(self.apikey)

    def _request(self, action, method, params=None):
        if params is None:
            params = {}
        url = 'https://' + self.host + '/' + self.version + '/' + self.apikey + '/' + action + '/' + method + '.json'
        try:
            content = requests.post(url, headers=self.headers, auth=None, data=params, timeout=self.timeout).content
            try:
                response = json.loads(content.decode("utf-8"))
                if response['return']['status'] == 200:
                    response = response['entries']
                else:
                    raise Exception(
                        'APIException[{}] {}'.format(response['return']['status'], response['return']['message']))
            except ValueError as e:
                raise Exception(e)
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(e)

    def sms_send(self, params=None):
        return self._request('sms', 'send', params)
