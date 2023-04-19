from lesson_19.utilities.web_ui.locators import Locator
from selenium.webdriver.common.by import By


class MainPageLocators:
    def __init__(self):
        self.__main_page_button = Locator(By.XPATH,
                                          '//*[text()="Main page" or  text()="Strona główna"]//ancestor::*[@role="button"]')
        self.__players_button = Locator(By.XPATH,
                                        '//*[text()="Players" or text()="Gracze"]//ancestor::*[@role="button"]')
        self.__pl_language_button = Locator(By.XPATH, '//*[text()="Polski"]//ancestor::*[@role="button"]')
        self.__en_language_button = Locator(By.XPATH, '//*[text()="English"]//ancestor::*[@role="button"]')
        self.__sign_out_button = Locator(By.XPATH,
                                         '//*[text()="Sign out" or text()="Wyloguj"]//ancestor::*[@role="button"]')
        self.__add_player_button = Locator(By.XPATH, '//a[contains(@href, "/players/add")]/button')
        self.__dev_contact_link = Locator(By.XPATH, '//a[contains(@href, "https://app.slack.com/")]')
        self.__logo = Locator(By.XPATH, '//*[@title="Logo Scouts Panel"]')
        self.__header = Locator(By.XPATH, '//h2[text()="Scouts Panel"]')
        self.__last_cr_player_button = Locator(By.XPATH, '//a[1][contains(@href, "edit")]/button')
        self.__last_upd_player_button = Locator(By.XPATH, '//a[2][contains(@href, "edit")]/button')
        self.__last_cr_match_button = Locator(By.XPATH, '//a[3][contains(@href, "match")]/button')

    @property
    def main_page_button(self):
        return self.__main_page_button.get_locator()

    @property
    def players_button(self):
        return self.__players_button.get_locator()

    @property
    def en_language_button(self):
        return self.__en_language_button.get_locator()

    @property
    def pl_language_button(self):
        return self.__pl_language_button.get_locator()

    @property
    def sign_out_button(self):
        return self.__sign_out_button.get_locator()

    @property
    def dev_contact_link(self):
        return self.__dev_contact_link.get_locator()

    @property
    def logo(self):
        return self.__logo.get_locator()

    @property
    def last_cr_player_button(self):
        return self.__last_cr_player_button.get_locator()

    @property
    def last_upd_player_button(self):
        return self.__last_upd_player_button.get_locator()

    @property
    def last_cr_match_button(self):
        return self.__last_cr_match_button.get_locator()

    @property
    def add_player_button(self):
        return self.__add_player_button.get_locator()
