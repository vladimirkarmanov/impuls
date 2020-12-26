from typing import Dict

import requests
from django.conf import settings


class Moodle:
    MOODLE_HOST = settings.MOODLE_HOST
    AUTH_URL = '/login/token.php?username=moadmin&password=Fs$38fjskdffj&service=impuls'
    BASE_URL = '/webservice/rest/server.php'
    ADMIN_LOGIN = 'moadmin'
    ADMIN_PASS = 'Fs$38fjskdffj'

    def _prepare_url(self, moodle_func: str, wstoken: str = 'ddb7888cf6edb99cacd418b1dd59b409'):
        return f'{self.MOODLE_HOST}{self.BASE_URL}?wstoken={wstoken}&wsfunction={moodle_func}&moodlewsrestformat=json'

    def get_service_token(self) -> str:
        params = {
            'username': settings.MOODLE_USERNAME,
            'password': settings.MOODLE_PASSWORD
        }
        r = requests.get(f'{self.MOODLE_HOST}{self.AUTH_URL}', params=params)
        return r.json().get('token')

    def signup_user(self, data: Dict[str, str]) -> None:
        requests.post(self._prepare_url('auth_email_signup_user'), data=data)

    # TODO: активировать аккаунт
