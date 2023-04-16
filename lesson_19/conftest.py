import pytest
import json

from lesson_19.constants import PATH_TO_PROJECT
from lesson_19.page_objects.add_player_page_pack.add_player_page import AddPlayerPage
from lesson_19.utilities.configurations import Configuration
from utilities.driver_factory import driver_factory
from lesson_19.page_objects.login_page_pack.login_page import LoginPage
from lesson_19.page_objects.main_page_pack.main_page import MainPage


@pytest.fixture()
def create_browser(env):
    driver = driver_factory(int(env.browser_id))
    driver.maximize_window()
    driver.get(env.site_url_en)
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_browser):
    return LoginPage(create_browser)


@pytest.fixture()
def open_main_page(open_login_page, env):
    open_login_page.login(email=env.email, password=env.password)
    return MainPage(open_login_page.driver)


@pytest.fixture()
def login_with_invalid_pass(open_login_page, env):
    return open_login_page.login(env.password, 'test')


@pytest.fixture()
def open_add_player_page(open_main_page):
    open_main_page.click_add_player_button()
    return AddPlayerPage(open_main_page.driver)


@pytest.fixture(scope='session', autouse=True)
def env():
    with open(f'{PATH_TO_PROJECT}/configurations/config.json', 'r') as file:
        result = file.read()
    config = json.loads(result)
    return Configuration(**config)
