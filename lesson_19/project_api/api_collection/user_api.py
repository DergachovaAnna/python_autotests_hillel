from lesson_19.utilities.api.base_api import BaseApi


class UserApi(BaseApi):
    def __init__(self, env):
        super().__init__(env)
        self.__endpoint = '/user/'

    def create_user(self):
        pass

    def user_login(self):
        pass

    def user_logout(self):
        pass

    def update_user(self):
        pass

    def delete_user(self):
        pass
