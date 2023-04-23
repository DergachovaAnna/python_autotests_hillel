import time

import pytest


def test_download_file_csv(open_main_page):  # this test will not work in case browser runned as 'headless'
    result = open_main_page.click_players_button().download_csv_data()
    assert result is not None, "File was not found in 'Downloads' folder"


# def test_search_player(open_main_page):
#     open_main_page.click_add_player_button().add_player_with_required_fields()
#     pass
