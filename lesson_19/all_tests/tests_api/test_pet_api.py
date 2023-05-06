import random
import json
import pytest



@pytest.mark.smoke_api
@pytest.mark.ci
def test_add_new_pet(set_up_pet):
    pet_data = {"pet_id": random.randint(1, 100000000), "name": "test_pet"}
    response = set_up_pet.add_new_pet(**pet_data)
    assert response.status_code == 200, 'New pet was not created'
    response_data = response.json()

    assert response_data['name'] == pet_data['name'], 'Name of the created pet does not match'
    assert response_data['id'] == pet_data['pet_id'], 'ID of the created pet does not match'


def test_add_new_pet_without_required_fields(set_up_pet):
    pet_data = {"pet_id": None, "name": ""}
    response = set_up_pet.add_new_pet(**pet_data)
    assert response.status_code == 400, 'Pet was created without "name" and "id"'

@pytest.mark.ci
def test_update_pet(set_up_pet):
    set_up_pet.add_new_pet(**{"pet_id": random.randint(1, 100000000), "name": "Pet1"})
    new_pet_data = {"pet_id": 19933991, "name": "Pet2", "status": "unknown_status"}
    response = set_up_pet.update_pet(**new_pet_data)

    # verify that the update was successful
    assert response.status_code == 200, 'Failed to update the pet'
    response_data = response.json()
    assert response_data['name'] == new_pet_data["name"], 'Failed to update the name of the pet'
    assert response_data['status'] == new_pet_data["status"], 'Failed to update the name of the pet'

@pytest.mark.ci
def test_get_pet_by_id(set_up_pet):
    # create pet
    created_pet = set_up_pet.add_new_pet(**{"pet_id": random.randint(1, 100000000), "name": "Pet3"})
    created_pet_json_data = json.loads(created_pet.text)

    # search  by created pet ID
    response = set_up_pet.get_pet_by_id(created_pet_json_data["id"])
    json_data_response = json.loads(response.text)
    assert response.status_code == 200, 'Pet not found'
    assert json_data_response["id"] == created_pet_json_data["id"], 'Created and searched pet id are not match'
    assert json_data_response["name"] == created_pet_json_data["name"], 'Created and searched pet name are not match'

@pytest.mark.ci
def test_delete_pet(set_up_pet):
    # crete pet first
    created_pet = set_up_pet.add_new_pet(**{"pet_id": random.randint(1, 100000000), "name": "Pet3"})
    created_pet_json_data = json.loads(created_pet.text)

    # delete created pet by ID
    response = set_up_pet.delete_pet(created_pet_json_data["id"])
    assert response.status_code == 200, 'Pet was not removed or not found'

    # verify status code 404 if ID was already removed
    response = set_up_pet.delete_pet(created_pet_json_data["id"])
    assert response.status_code == 404, 'Status code is not as expected'
