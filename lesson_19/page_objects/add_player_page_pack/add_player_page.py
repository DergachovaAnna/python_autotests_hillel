from datetime import datetime
from lesson_19.page_objects.add_player_page_pack.add_player_locators import AddPlayerPageLocators
from lesson_19.page_objects.matches_page_pack.matches_page import MatchesPage
from lesson_19.utilities.web_ui.base_page import BasePage
from faker import Faker
import random


class AddPlayerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__page_locator = AddPlayerPageLocators()
        self.__faker_data = Faker()
        self.__player_name = self.__faker_data.name()

    @property
    def player_name(self):
        return self.__player_name

    def send_email(self):
        email = self.__faker_data.email()
        self.send_keys(locator=self.__page_locator.email_input, value=email)
        return self

    def send_name(self):
        self.send_keys(locator=self.__page_locator.name_input, value=self.__player_name)
        return self

    def send_surname(self):
        surname = self.__faker_data.last_name()
        self.send_keys(locator=self.__page_locator.surname_input, value=surname)
        return self

    def send_age(self):
        dob = self.__faker_data.date_of_birth()
        formatted_dob = datetime.strftime(dob, '%d-%m-%Y')
        self.send_keys(locator=self.__page_locator.age_select, value=formatted_dob)
        return self

    def send_main_position(self):
        positions = ['Goalkeeper', 'Defender', 'Midfielder', 'Forward']
        self.send_keys(locator=self.__page_locator.main_position_input, value=random.choice(positions))
        return self

    def click_submit_button(self):
        self.click(self.__page_locator.submit_button)
        return self

    def add_player_with_required_fields(self):
        self.send_email().send_name().send_surname().send_main_position().send_age().click_submit_button()
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
        self.wait_until_element_located(locator=self.__page_locator.player_added_sucess_popup)
        element = self.find_element(*self.__page_locator.player_added_sucess_popup)
        if element is not None:
            return element.text
        else:
            return None

    def add_player_without_age(self):
        self.send_email().send_name().send_surname().send_main_position()
        self.click_submit_button().wait_for_add_player_confirmation_popup()
        return self

    def validate_email(self):
        email_list = ['abc@', '@gmail.com', 'abc', 'abc@gmail', 'abd@gmail.']
        for email_data in email_list:
            self.send_keys(self.__page_locator.email_input, email_data)
            self.send_name().send_surname().send_age().send_main_position().click_submit_button()
            self.clear_fields_js(self.__page_locator.email_input)
        return self

    def click_matches_button(self):
        self.click(self.__page_locator.matches_button)
        return MatchesPage(self.driver)



