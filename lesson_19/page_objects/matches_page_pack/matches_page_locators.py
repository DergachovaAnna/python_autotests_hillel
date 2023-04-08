from selenium.webdriver.common.by import By
from lesson_19.utilities.web_ui.locators import Locator


class MatchesPageLocators:
    def __init__(self):
        self.__add_match_button = Locator(By.XPATH, '//*[text()="Add match" or text()="Dodaj mecz"]/parent::button')
        self.__my_team_input = Locator(By.XPATH, '//input[@name="myTeam"]')
        self.__enemy_team_input = Locator(By.XPATH, '//input[@name="enemyTeam"]')
        self.__my_team_score_input = Locator(By.XPATH, '//input[@name="myTeamScore"]')
        self.__enemy_team_score_input = Locator(By.XPATH, '//input[@name="enemyTeamScore"]')
        self.__match_date_input = Locator(By.XPATH, '//input[@name="date"]')
        self.__match_at_home_radio_button = Locator(By.XPATH, '//span[text()="Match at home" /'
                                                              'or text()="Mecz domowy"]//preceding-sibling::span')
        self.__match_out_of_home_radio_button = Locator(By.XPATH, '//span[text()="Mecz wyjazdowy" /'
                                                                  'or text()="Match out home"]//preceding-sibling::span')

        self.__submit_button = Locator(By.XPATH, '//*[@type="submit"]')
        self.__clear_button = Locator(By.XPATH, '//button//*[text()="Clear"]')
        self.__last_added_match_row = Locator(By.XPATH, '//tbody/tr[last()]')
        self.__last_added_match_edit_button = Locator(By.XPATH, '//tbody/tr[last()]//a[contains(@href, "edit")]')
        self.__added_match_my_team_name = Locator(By.XPATH, f'//tbody/tr[last()]/td[text()={{my_team_name}}]')



    @property
    def add_match_button(self):
        return self.__add_match_button.get_locator()


    @property
    def my_team_input(self):
        return self.__my_team_input.get_locator()

    @property
    def enemy_team_input(self):
        return self.__enemy_team_input.get_locator()

    @property
    def my_team_score_input(self):
        return self.__my_team_score_input.get_locator()

    @property
    def enemy_team_score_input(self):
        return self.__enemy_team_score_input.get_locator()

    @property
    def match_date_input(self):
        return self.__match_date_input.get_locator()

    @property
    def match_at_home_radio_button(self):
        return self.__match_at_home_radio_button.get_locator()

    @property
    def submit_button(self):
        return self.__submit_button.get_locator()

    @property
    def clear_button(self):
        return self.__clear_button.get_locator()

    @property
    def last_added_match_row(self):
        return self.__last_added_match_row.get_locator()

    @property
    def last_added_match_edit_button(self):
        return self.__last_added_match_edit_button.get_locator()

    @property
    def added_match_my_team_name(self):
        return self.__added_match_my_team_name.get_locator()
