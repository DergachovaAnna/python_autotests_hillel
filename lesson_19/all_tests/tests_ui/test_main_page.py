import re
import pytest


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.ci
def test_sign_out(open_main_page):
    open_main_page.click_sign_out()
    assert open_main_page.get_title() == "Scouts panel - sign in", "Main page was not opened"


@pytest.mark.smoke
@pytest.mark.ci
def test_find_elements(open_main_page):  # to verify that desired elements are on the page
    assert len(open_main_page.find_elements_on_page()) == 5, "Some elements are missing on the main page"


@pytest.mark.regression
@pytest.mark.ci
def test_menu_navigation(open_main_page):
    open_main_page.click_main_page_button()
    assert open_main_page.find_main_page_logo() is not None, "Element not found"

    players_page_url = open_main_page.click_players_button().driver.current_url
    assert players_page_url.endswith("/players"), f"Received not expected URL: {players_page_url}"

    add_player_page_url_ = open_main_page.click_main_page_button().click_add_player_button().driver.current_url
    assert add_player_page_url_.endswith("/players/add"), f"Received not expected URL: {add_player_page_url_}"

    pattern = r'/players/.+/edit$'  # pattern to search for url that ends as /players/{{player id}}/edit
    edit_player_url = open_main_page.click_main_page_button().click_last_created_player().driver.current_url
    match = re.search(pattern, edit_player_url)
    assert match is not None, f"Expected a URL that matches the pattern {pattern}, but instead received URL: {edit_player_url}"


@pytest.mark.regression
@pytest.mark.ci
def test_change_language(open_main_page):
    current_url = open_main_page.driver.current_url
    open_main_page.click_language_button()
    new_url = open_main_page.driver.current_url
    if current_url.endswith("pl"):
        assert new_url.endswith("en"), f"Language was not changed, page URL is: {new_url}"
    elif current_url.endswith("en"):
        assert new_url.endswith("pl"), f"Language was not changed, page URL is: {new_url}"



