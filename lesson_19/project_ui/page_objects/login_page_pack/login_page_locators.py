from lesson_19.utilities.web_ui.locators import Locator
from selenium.webdriver.common.by import By


class LoginPageLocators:

    def __init__(self):
        self.__login_input = Locator(By.CSS_SELECTOR, '#login')
        self.__password_input = Locator(By.CSS_SELECTOR, '#password')
        self.__sign_in_button = Locator(By.XPATH, '//*[text()="Sign in" or text()="Zaloguj"]')
        self.__header_text = Locator(By.XPATH, '//*[text()="Scouts Panel"]')
        self.__language_list = Locator(By.XPATH, '//div[contains(@aria-haspopup, "listbox")]')
        self.__language_english = Locator(By.XPATH, '//*[@id="menu-"]//*[@data-value="en"]')
        self.__language_polish = Locator(By.XPATH, '//*[@id="menu-"]//*[@data-value="pl"]')
        self.__login_label = Locator(By.CSS_SELECTOR, '#login-label')
        self.__password_label = Locator(By.CSS_SELECTOR, '#password-label')
        self.__password_error_message = Locator(By.XPATH, '//span[text()="Identifier or password invalid."]')
        self.__remind_password_button = Locator(By.XPATH, '//form//a')
        self.__remind_pass_email_input = Locator(By.XPATH, '//*[@name="email"]')
        self.__remind_pass_send_button = Locator(By.XPATH, '//*[text()="Send" or text()="Wyślij"]')
        self.__remind_pass_confirmation_popup = Locator(By.CSS_SELECTOR, 'div.Toastify__toast-body')
        self._remind_pass_confirmation_text = 'div.Toastify__toast-body'
        self.__back_to_sign_in_button = Locator(By.XPATH, '//*/a')

    @property
    def login_input(self):
        return self.__login_input.get_locator()

    @property
    def password_input(self):
        return self.__password_input.get_locator()

    @property
    def sign_in_button(self):
        return self.__sign_in_button.get_locator()

    @property
    def header_text(self):
        return self.__header_text.get_locator()

    @property
    def language_list(self):
        return self.__language_list.get_locator()

    @property
    def language_english(self):
        return self.__language_english.get_locator()

    @property
    def language_polish(self):
        return self.__language_polish.get_locator()

    @property
    def login_label(self):
        return self.__login_label.get_locator()

    @property
    def password_label(self):
        return self.__password_label.get_locator()

    @property
    def password_error_message(self):
        return self.__password_error_message.get_locator()

    @property
    def remind_password_button(self):
        return self.__remind_password_button.get_locator()

    @property
    def remind_pass_email_input(self):
        return self.__remind_pass_email_input.get_locator()

    @property
    def remind_pass_send_button(self):
        return self.__remind_pass_send_button.get_locator()

    @property
    def remind_pass_confirmation_popup(self):
        return self.__remind_pass_confirmation_popup.get_locator()

    @property
    def back_to_sign_in_button(self):
        return self.__back_to_sign_in_button.get_locator()
