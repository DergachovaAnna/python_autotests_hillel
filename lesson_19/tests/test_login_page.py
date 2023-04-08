from lesson_19.utilities.config_reader import get_site_url
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_successful_login(open_main_page):
    expected_title = 'Scouts panel'
    assert expected_title in open_main_page.get_title()


@pytest.mark.smoke
@pytest.mark.regression
def test_fail_login_to_system(login_with_invalid_pass):
    expected_text = 'Identifier or password invalid.'
    assert expected_text in login_with_invalid_pass.get_password_error_message()  # check validation message
    assert login_with_invalid_pass.driver.current_url == get_site_url()  # check that I stay on login page


@pytest.mark.regression
def test_remind_password(open_login_page):
    text = (open_login_page.click_remind_password()
            .send_email_remind_pass('example@example.com')
            .click_to_submit_remind_pass_js()
            .wait_for_remind_pass_confirmation_popup())
    assert text == 'Message sent successfully.' or text == 'Wysłano wiadomość na podany adres e-mail.'


@pytest.mark.regression
def test_navigation_from_remind_pass_page(open_login_page):
    page = open_login_page.click_remind_password().click_back_to_sign_in_button()
    assert page.get_title() == "Scouts panel - sign in" or page.get_title() == "Scouts panel - zaloguj"


@pytest.mark.regression
def test_change_language_english(open_login_page):
    text = open_login_page.change_language('EN').get_signin_button_text()
    assert text == "SIGN IN"


@pytest.mark.regression
def test_change_language_polish(open_login_page):
    text = open_login_page.change_language('pl').get_signin_button_text()
    assert text == "ZALOGUJ"