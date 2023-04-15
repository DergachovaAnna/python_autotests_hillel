import pytest

from lesson_19.page_objects.add_player_page_pack.add_player_page import AddPlayerPage
from utilities.config_reader import get_site_url, get_browser_id, get_user_creds
from utilities.driver_factory import driver_factory
from lesson_19.page_objects.login_page_pack.login_page import LoginPage
from lesson_19.page_objects.main_page_pack.main_page import MainPage


@pytest.fixture()
def create_browser():
    driver = driver_factory(get_browser_id())
    driver.maximize_window()
    driver.get(get_site_url()[0])
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_browser):
    return LoginPage(create_browser)


@pytest.fixture()
def open_main_page(open_login_page):
    open_login_page.login(get_user_creds()[0], get_user_creds()[1])
    return MainPage(open_login_page.driver)


@pytest.fixture()
def login_with_invalid_pass(open_login_page):
    return open_login_page.login(get_user_creds()[0], 'test')


@pytest.fixture()
def open_add_player_page(open_main_page):
    open_main_page.click_add_player_button()
    return AddPlayerPage(open_main_page.driver)
