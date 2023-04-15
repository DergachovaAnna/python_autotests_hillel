from lesson_19.utilities.web_ui.locators import Locator
from selenium.webdriver.common.by import By


class AddPlayerPageLocators:
    def __init__(self):
        self.__email_input = Locator(By.XPATH, '//*[@name="email"]')
        self.__name_input = Locator(By.XPATH, '//*[@name="name"]')
        self.__surname_input = Locator(By.XPATH, '//*[@name="surname"]')
        self.__phone_input = Locator(By.XPATH, '//*[@name="phone"]')
        self.__age_select = Locator(By.XPATH, '//*[@name="age"]')
        self.__main_position_input = Locator(By.XPATH, '//*[@name="mainPosition"]')
        self.__player_added_success_popup = Locator(By.XPATH, '//*[text()="Added player." or text()="Dodano gracza."]')
        self.__submit_button = Locator(By.XPATH, '//*[@type="submit"]')
        self.__add_language_button = Locator(By.XPATH, '//*[text()="Dodaj język" or text()="Add language"]')
        self.__edit_player_text = Locator(By.XPATH, '//*[@class="MuiCardHeader-content"]/*[contains(text(), '
                                                    '"Edycja gracza") or contains(text(), "Edit player")]')
        self.__matches_button = Locator(By.XPATH, '//*[text()="Matches" or text()="Mecze"]')

    @property
    def edit_player_text(self):
        return self.__edit_player_text.get_locator()

    @property
    def matches_button(self):
        return self.__matches_button.get_locator()

    @property
    def email_input(self):
        return self.__email_input.get_locator()

    @property
    def name_input(self):
        return self.__name_input.get_locator()

    @property
    def surname_input(self):
        return self.__surname_input.get_locator()

    @property
    def phone_input(self):
        return self.__phone_input.get_locator()

    @property
    def age_select(self):
        return self.__age_select.get_locator()

    @property
    def main_position_input(self):
        return self.__main_position_input.get_locator()

    @property
    def player_added_sucess_popup(self):
        return self.__player_added_success_popup.get_locator()

    @property
    def submit_button(self):
        return self.__submit_button.get_locator()

    @property
    def add_language_button(self):
        return self.__add_language_button.get_locator()
