import pytest
from selenium.common.exceptions import TimeoutException


@pytest.mark.regression
def test_add_player_with_required_fields(open_add_player_page):
    assert open_add_player_page.is_required_fields_empty(), "Required fields are not empty before sending data"
    text = open_add_player_page.add_player_with_required_fields().wait_for_add_player_confirmation_popup()
    assert text == 'Added player.' or text == 'Dodano gracza.'


@pytest.mark.regression
def test_add_player_without_age(open_add_player_page):
    try:
        open_add_player_page.add_player_without_age()
        assert False, "Confirmation popup is displayed when it shouldn't be"
    except TimeoutException:
        assert True


# Code does not work correct: input field is cleared, but then instead of sending next email value from the list,
# input is a concatenated value of previous and next values
# def test_create_record_with_invalid_email(open_add_player_page):
#     page = open_add_player_page
#     email_list = ['abc@', '@fghj', 'abc', 'abc@gmail.']
#     email_field_locator = (By.XPATH, '//*[@name="email"]')
#     for email_data in email_list:
#         page.send_keys(email_field_locator, email_data)
#         time.sleep(5)
#         page.click_submit_button()
#         page.clear_fields_js(email_field_locator)
#         time.sleep(5)
#     assert open_add_player_page.get_title() == "Add player" or open_add_player_page.get_title() == "Dodaj gracza"
#

