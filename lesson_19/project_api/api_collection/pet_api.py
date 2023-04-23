from lesson_19.project_api.data_objects.pet_data import Pet
from lesson_19.utilities.api.base_api import BaseApi


class PetApi(BaseApi):
    def __init__(self, env):
        super().__init__(env)
        self.__endpoint = '/pet/'
        self.__headers = {'accept': 'application/json', 'api_key': '9876543234567876543'}

    def add_new_pet(self, **kwargs):
        response = self.post(endpoint=f'{self.__endpoint}', payload=Pet(**kwargs).create_payload())
        return response

    def update_pet(self, pet_id, name, **kwargs):  # update pet name and status, using same pet ID
        updated_pet = Pet(pet_id, name, status=kwargs.get('status', None)).update_data(**kwargs)
        response = self.put(endpoint=f'{self.__endpoint}', payload=updated_pet.create_payload())
        return response

    def get_pet_by_id(self, pet_id):
        response = self.get(endpoint=f'{self.__endpoint}{pet_id}')
        return response

    def delete_pet(self, pet_id):
        response = self.delete(endpoint=f'{self.__endpoint}{pet_id}', headers=self.__headers)
        return response
