import requests


class BaseApi:
    def __init__(self, env):
        self.__request = requests
        self.__base_url = env.base_api_url
        self.__headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

    def get(self, endpoint, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.get(f'{self.__base_url}{endpoint}', headers=headers)
        return response

    def post(self, endpoint, payload, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.post(f'{self.__base_url}{endpoint}', data=payload, headers=headers)
        return response

    def put(self, endpoint, payload, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.put(f'{self.__base_url}{endpoint}', data=payload, headers=headers)
        return response

    def delete(self, endpoint, headers):
        if headers is None:
            headers = self.__headers
        response = self.__request.delete(f'{self.__base_url}{endpoint}', headers=headers)
        return response
