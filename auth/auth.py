from db.local_db import DataBase
from config import API_HOST
from models import AuthModel
from requests import api


class Auth:
    def __init__(self):
        self.db = DataBase()

    def get_local_session(self):
        access, refresh = self.db.get('access'), self.db.get('refresh')
        if access and refresh:
            return AuthModel({
                'access': access,
                'refresh': refresh
            })

    def get_header(self):
        return {"Authorization": f"Bearer {self.get_local_session().access}"}

    def login(self, username: str, password: str) -> AuthModel | None:
        path = API_HOST / 'auth/login/'
        request = api.post(path, {'username': username, 'password': password})
        if request.status_code == 200:
            response = request.json()
            self.db.set('access', response.get('access'))
            self.db.set('refresh', response.get('refresh'))
            return self.get_local_session()

    def is_login(self):
        if self.get_local_session():
            if self.refresh_access():
                return True

    def refresh_access(self):
        path = API_HOST / 'auth/login/refresh/'
        request = api.post(path, data={'refresh': self.db.get('refresh')})
        if request.status_code == 200:
            self.db.set('access', request.json().get('access'))
            return True
        else:
            raise 'login req'

