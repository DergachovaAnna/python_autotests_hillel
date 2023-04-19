from lesson_19.project_ui.page_objects.matches_page_pack.matches_page_locators import MatchesPageLocators
from lesson_19.utilities.web_ui.base_page import BasePage
from faker import Faker
import random
from datetime import datetime


class MatchesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__page_locator = MatchesPageLocators()
        self.__faker_data = Faker()

    def click_add_match(self):
        self.click(self.__page_locator.add_match_button)
        return self

    def set_my_team_name(self):
        self.send_keys(self.__page_locator.my_team_input, 'Team 1')
        return self

    def set_enemy_team_name(self):
        self.send_keys(self.__page_locator.enemy_team_input, 'Team 2')
        return self

    def set_my_team_score(self):
        my_score = random.randint(0, 100)
        self.send_keys(self.__page_locator.my_team_score_input, my_score)
        return self

    def set_enemy_team_score(self):
        enemy_score = random.randint(0, 100)
        self.send_keys(self.__page_locator.enemy_team_score_input, enemy_score)
        return self

    def set_match_date(self):
        random_date = self.__faker_data.date_between(start_date='-3y', end_date='today')
        formatted_date = datetime.strftime(random_date, '%d-%m-%Y')
        self.send_keys(self.__page_locator.match_date_input, formatted_date)
        return self

    def click_submit_match_form(self):
        self.click(self.__page_locator.submit_button)
        return self

    def create_match(self):
        self.click_add_match()
        self.set_my_team_name().set_enemy_team_name().set_my_team_score().set_enemy_team_score().set_match_date()
        self.click_submit_match_form()
        self.wait_until_element_located(self.__page_locator.last_added_match_row)
        return self

    def find_last_added_match(self):
        return self.find_element(*self.__page_locator.last_added_match_row)
