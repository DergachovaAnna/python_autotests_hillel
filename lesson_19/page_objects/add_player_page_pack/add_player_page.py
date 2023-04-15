import time
from datetime import datetime
from lesson_19.page_objects.add_player_page_pack.add_player_locators import AddPlayerPageLocators
from lesson_19.page_objects.matches_page_pack.matches_page import MatchesPage
from lesson_19.utilities.web_ui.base_page import BasePage
from faker import Faker
import random
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys


class AddPlayerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__page_locator = AddPlayerPageLocators()
        self.__faker_data = Faker()
        self.__player_name = self.__faker_data.name()

    @property
    def player_name(self):
        return self.__player_name

    def set_email(self):
        email = self.__faker_data.email()
        self.send_keys(locator=self.__page_locator.email_input, value=email)
        return self

    def set_name(self):
        self.send_keys(locator=self.__page_locator.name_input, value=self.__player_name)
        return self

    def set_surname(self):
        surname = self.__faker_data.last_name()
        self.send_keys(locator=self.__page_locator.surname_input, value=surname)
        return self

    def set_age(self):
        dob = self.__faker_data.date_of_birth()
        formatted_dob = datetime.strftime(dob, '%d-%m-%Y')
        self.send_keys(locator=self.__page_locator.age_select, value=formatted_dob)
        return self

    def set_main_position(self):
        positions = ['Goalkeeper', 'Defender', 'Midfielder', 'Forward']
        self.send_keys(locator=self.__page_locator.main_position_input, value=random.choice(positions))
        return self

    def click_submit_button(self):
        self.click(self.__page_locator.submit_button)
        return self

    def add_player_with_required_fields(self):
        self.set_email().set_name().set_surname().set_main_position().set_age().click_submit_button()
        return self

    def is_required_fields_empty(self):
        name_input = self.find_element(*self.__page_locator.name_input)
        surname_input = self.find_element(*self.__page_locator.surname_input)
        age_input = self.find_element(*self.__page_locator.age_select)
        email_input = self.find_element(*self.__page_locator.email_input)
        main_position_input = self.find_element(*self.__page_locator.main_position_input)

        if not name_input.get_attribute("value") and \
                not surname_input.get_attribute("value") and \
                not age_input.get_attribute("value") and \
                not main_position_input.get_attribute("value") and \
                not email_input.get_attribute("value"):
            return True
        else:
            return False

    def wait_for_add_player_confirmation_popup(self):
        element_text = self.get_text(self.__page_locator.player_added_sucess_popup)
        if element_text is None:
            return None
        else:
            return element_text

    def add_player_without_age(self):
        self.set_email().set_name().set_surname().set_main_position()
        self.click_submit_button().wait_for_add_player_confirmation_popup()
        return self

    def set_invalid_email_format(self, email_data):
        email_input = self.find_element(*self.__page_locator.email_input)
        for letter in range(len(email_data)):  # clear the field multiple times
            email_input.send_keys(Keys.BACKSPACE)
        email_input.send_keys(email_data)
        return self

    def validate_email(self, email_list):
        for email_data in email_list:
            self.set_name().set_surname().set_age().set_main_position()
            self.set_invalid_email_format(email_data)
            self.click_submit_button()
        return self

    def click_matches_button(self):
        self.click(self.__page_locator.matches_button)
        return MatchesPage(self.driver)
