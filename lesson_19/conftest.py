from contextlib import suppress
import allure
import psycopg2
import pytest
import json
from lesson_19.constants import PATH_TO_PROJECT
from lesson_19.project_api.api_collection.pet_api import PetApi
from lesson_19.project_api.api_collection.store_api import StoreApi
from lesson_19.project_ui.page_objects.add_player_page_pack.add_player_page import AddPlayerPage
from lesson_19.utilities.configurations import Configuration
from lesson_19.utilities.driver_factory import driver_factory
from lesson_19.project_ui.page_objects.login_page_pack.login_page import LoginPage
from lesson_19.project_ui.page_objects.main_page_pack.main_page import MainPage


def pytest_addoption(parser):
    parser.addoption('--browser_id', action='store', default=1, help='Set browser id')


@pytest.fixture(scope='session', autouse=True)
def env():
    with open(f'{PATH_TO_PROJECT}/configurations/config.json', 'r') as file:
        result = file.read()
    config = json.loads(result)
    return Configuration(**config)


@pytest.fixture()
def create_browser(env, pytestconfig, request):
    driver = driver_factory(int(pytestconfig.getoption('--browser_id')))
    driver.maximize_window()
    driver.get(env.site_url_en)

    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


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


@pytest.fixture()
def set_up_pet(env):
    return PetApi(env)


@pytest.fixture()
def set_up_store(env):
    return StoreApi(env)


@pytest.fixture()
def create_db_connection(env):
    connection = psycopg2.connect(user=env.db_user,
                                  password=env.db_password,
                                  host=env.host,
                                  port=env.port,
                                  database=env.db_name)
    cursor = connection.cursor()
    yield connection, cursor
    if cursor:
        connection.close()
        cursor.close()
