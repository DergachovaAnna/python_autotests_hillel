# will be expanded later

def test_add_new_pet(set_up_store):
    response = set_up_store.place_pet_order()
    assert response.status_code == 200, 'Status code is not as expected'
