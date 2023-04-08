import time

import pytest


def test_download_file_csv(open_main_page):
    result = open_main_page.click_players_button().download_csv_data()
    assert result is not None


# def test_search_player(open_main_page):
#     open_main_page.click_add_player_button().add_player_with_required_fields()
#     pass



