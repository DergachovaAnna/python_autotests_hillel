import pytest
import json
from lesson_19.constants import PATH_TO_PROJECT
from lesson_19.project_api.api_collection.pet_api import PetApi
from lesson_19.project_api.api_collection.store_api import StoreApi
# from lesson_19.project_ui.page_objects.add_player_page_pack.add_player_page import AddPlayerPage
from lesson_19.utilities.configurations import Configuration
from lesson_19.utilities.driver_factory import driver_factory
# from lesson_19.project_ui.page_objects.login_page_pack.login_page import LoginPage
# from lesson_19.project_ui.page_objects.main_page_pack.main_page import MainPage


def pytest_addoption(parser):
    parser.addoption('--browser_id', action='store', default=1, help='Set browser id')


@pytest.fixture()
def create_browser(env, pytestconfig):
    driver = driver_factory(int(pytestconfig.getoption('--browser_id')))
    driver.maximize_window()
    driver.get(env.site_url_en)
    yield driver
    driver.quit()


# @pytest.fixture()
# def open_login_page(create_browser):
#     return LoginPage(create_browser)


# @pytest.fixture()
# def open_main_page(open_login_page, env):
#     open_login_page.login(email=env.email, password=env.password)
#     return MainPage(open_login_page.driver)


@pytest.fixture()
def login_with_invalid_pass(open_login_page, env):
    return open_login_page.login(env.password, 'test')


# @pytest.fixture()
# def open_add_player_page(open_main_page):
#     open_main_page.click_add_player_button()
#     return AddPlayerPage(open_main_page.driver)


@pytest.fixture(scope='session', autouse=True)
def env():
    with open(f'{PATH_TO_PROJECT}/configurations/config.json', 'r') as file:
        result = file.read()
    config = json.loads(result)
    return Configuration(**config)


@pytest.fixture()
def set_up_pet(env):
    return PetApi(env)


@pytest.fixture()
def set_up_store(env):
    return StoreApi(env)
