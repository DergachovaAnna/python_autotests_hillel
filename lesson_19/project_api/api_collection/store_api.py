from lesson_19.project_api.data_objects.store_data import Store
from lesson_19.utilities.api.base_api import BaseApi


class StoreApi(BaseApi):
    def __init__(self, env):
        super().__init__(env)
        self.__endpoint = '/store/order'

    def place_pet_order(self):
        response = self.post(endpoint=f'{self.__endpoint}', payload=Store().get_json())
        return response

    def find_purchase_by_id(self):
        pass

    def delete_purchase_order_by_id(self):
        pass
