import pytest


@pytest.mark.regression
@pytest.mark.ci
def test_add_match(open_add_player_page):
    created_match = open_add_player_page.add_player_with_required_fields().click_matches_button().create_match()
    assert created_match.find_last_added_match().is_displayed(), "Added match is not found in Matches table"
