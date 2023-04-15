import time

from lesson_19.page_objects.main_page_pack.main_page_locators import MainPageLocators
from lesson_19.page_objects.players_page_pack.players_page import PlayersPage
from lesson_19.utilities.web_ui.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from lesson_19.page_objects.add_player_page_pack.add_player_page import AddPlayerPage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__page_locator= MainPageLocators()

    def click_sign_out(self):
        self.click(self.__page_locator.sign_out_button)
        return self

    def find_elements_on_page(self):
        elements_to_check = [
            self.__page_locator.logo,
            self.__page_locator.dev_contact_link,
            self.__page_locator.last_cr_match_button,
            self.__page_locator.players_button,
            self.__page_locator.last_cr_player_button

        ]
        found_elements = []
        for element in elements_to_check:
            try:
                element = self.wait_until_element_located(element)
                found_elements.append(element)
            except NoSuchElementException:
                pass
        return found_elements

    def click_players_button(self):
        self.click(self.__page_locator.players_button)
        self.wait_for_url("/players")
        return PlayersPage(self.driver)

    def click_main_page_button(self):
        self.click(self.__page_locator.main_page_button)
        self.wait_until_element_located(self.__page_locator.logo)
        return self

    def click_language_button(self):
        try:
            self.click(self.__page_locator.en_language_button)
        except NoSuchElementException:
            self.click(self.__page_locator.pl_language_button)
        return self

    def click_add_player_button(self):
        self.click(self.__page_locator.add_player_button)
        self.wait_for_url("/players/add")
        return AddPlayerPage(self.driver)

    def click_last_created_player(self):
        self.click(self.__page_locator.last_cr_player_button)
        self.wait_for_url("/edit")
        return self

    def find_main_page_logo(self):
        self.find_element(*self.__page_locator.logo)
        return self
