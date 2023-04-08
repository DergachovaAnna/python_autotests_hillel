from selenium.webdriver.common.by import By
from lesson_19.utilities.web_ui.locators import Locator


class PlayersPageLocators:
    def __init__(self):
        self.__search_input = Locator(By.XPATH, '//input[@placeholder="Search…"]')
        self.__player_name_text = Locator(By.XPATH, f'//tbody/tr/td/div[text()="{{player_name}}"]')
        self.__name_sorting_button = Locator(By.XPATH, '//button//*[text()="Name" or text()="Imię"]')
        self.__surname_sorting_button = Locator(By.XPATH, '//button//*[text()="Surname" or text()="Nazwisko"]')
        self.__age_sorting_button = Locator(By.XPATH, '//button//*[text()="Age" or text()="Wiek"]')
        self.__main_position_button = Locator(By.XPATH, '//button//*[text()="Main position" or text()="Pozycja"]')
        self.__club_sorting_button = Locator(By.XPATH, '//button//*[text()="Club" or text()="Klub"]')
        self.__rating_sorting_button = Locator(By.XPATH, '//button//*[text()="Rating" or text()="Recenzja"]')
        self.__matches_column_text = Locator(By.XPATH, '//thead//*[text()="Matches" or text()="Mecze"]')
        self.__reports_column_text = Locator(By.XPATH, '//thead//*[text()="Reports" or text()="Raporty"]')
        self.__download_csv_button = Locator(By.XPATH, '//*[@data-testid="Download CSV-iconButton"]')
        self.__view_columns_button = Locator(By.XPATH, '//*[@data-testid="View Columns-iconButton"]')
        self.__show_columns_menu = Locator(By.XPATH, '//fieldset/..')
        self.__show_columns_close_button = Locator(By.XPATH, '//button[@aria-label="Close"]')
        self.__name_checkbox = Locator(By.XPATH, '//fieldset//*[text()="Name" or text()="Imię"]/preceding-sibling::span')

    @property
    def search_input (self):
        return self.__search_input.get_locator()

    @property
    def player_name_text(self):
        return self.__player_name_text.get_locator()

    @property
    def name_sorting_button(self):
        return self.__name_sorting_button.get_locator()

    @property
    def surname_sorting_button(self):
        return self.__surname_sorting_button.get_locator()

    @property
    def age_sorting_button(self):
        return self.__age_sorting_button.get_locator()

    @property
    def main_position_button(self):
        return self.__main_position_button.get_locator()

    @property
    def club_sorting_button (self):
        return self.__club_sorting_button.get_locator()

    @property
    def rating_sorting_button(self):
        return self.__rating_sorting_button.get_locator()

    @property
    def matches_column_text(self):
        return self.__matches_column_text.get_locator()

    @property
    def reports_column_text(self):
        return self.__reports_column_text.get_locator()

    @property
    def download_csv_button(self):
        return self.__download_csv_button.get_locator()

    @property
    def view_columns_button(self):
        return self.__view_columns_button.get_locator()

    @property
    def show_columns_menu(self):
        return self.__show_columns_menu.get_locator()

    @property
    def show_columns_close_button(self):
        return self.__show_columns_close_button.get_locator()

    @property
    def name_checkbox(self):
        return self.__name_checkbox.get_locator()
