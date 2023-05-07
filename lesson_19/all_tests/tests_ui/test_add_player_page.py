import pytest
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By


@pytest.mark.regression
def test_add_player_with_required_fields(open_add_player_page):
    assert open_add_player_page.is_required_fields_empty(), "Required fields are not empty before sending data"
    text = open_add_player_page.add_player_with_required_fields().wait_for_add_player_confirmation_popup()
    assert text == 'Added player.' or text == 'Dodano gracza.', "Player was not added"


@pytest.mark.regression
@pytest.mark.ci
def test_add_player_without_age(open_add_player_page):
    try:
        open_add_player_page.add_player_without_age()
        assert False, "Confirmation popup is displayed when it shouldn't be"
    except TimeoutException:
        assert True

@pytest.mark.ci
def test_create_record_with_invalid_email(open_add_player_page):
    page = open_add_player_page
    email_list = ['abc', 'abc@', 'abc@gmail', 'abc@gmail.', 'abc@@gmail.com']
    page.validate_email(email_list)
    assert open_add_player_page.get_title() == "Add player" or open_add_player_page.get_title() == "Dodaj gracza", \
        "User was added with invalid email format"


# def test_add_player_without_required_fields(open_add_player_page):
#     try:
#         open_add_player_page.add_player_without_age()
#         assert False, "Confirmation popup is displayed when it shouldn't be"
#     except TimeoutException:
#         assert True
#
#     try:
#         open_add_player_page.add_player_without_main_position()
#         assert False, "Confirmation popup is displayed when it shouldn't be"
#     except TimeoutException:
#         assert True
#
#     try:
#         open_add_player_page.add_player_without_name()
#         assert False, "Confirmation popup is displayed when it shouldn't be"
#     except TimeoutException:
#         assert True
