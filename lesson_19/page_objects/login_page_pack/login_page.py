from lesson_19.page_objects.login_page_pack.login_page_locators import LoginPageLocators
from lesson_19.page_objects.main_page_pack.main_page import MainPage
from lesson_19.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__page_locator = LoginPageLocators()

    def set_login_email(self, email: str):
        self.send_keys(locator=self.__page_locator.login_input, value=email)
        return self

    def set_login_password(self, password: str):
        self.send_keys(locator=self.__page_locator.password_input, value=password)
        return self

    def click_login_button(self):
        self.click(self.__page_locator.sign_in_button)
        return MainPage(self.driver)

    def login(self, email, password):
        self.set_login_email(email)
        self.set_login_password(password)
        self.click_login_button()
        return self
        # MainPage(self.driver)

    def click_language_list(self):
        self.click(self.__page_locator.language_list)

    def select_english(self):
        self.click(self.__page_locator.language_english)

    def select_polish(self):
        self.click(self.__page_locator.language_polish)
        return self

    def change_language(self, language):
        language_locator = {
            'en': self.__page_locator.language_english,
            'pl': self.__page_locator.language_polish
        }
        self.click(self.__page_locator.language_list)
        self.click(language_locator[language.lower()])
        return self

    def click_remind_password(self):
        self.click(self.__page_locator.remind_password_button)
        return self

    def set_email_remind_pass(self, email: str):
        self.send_keys(locator=self.__page_locator.remind_pass_email_input, value=email)
        return self

    def click_to_submit_remind_pass(self):
        self.click(self.__page_locator.remind_pass_send_button)
        return self

    def click_to_submit_remind_pass_js(self):
        self.click_via_js(locator=self.__page_locator.remind_pass_send_button)
        return self

    def click_back_to_sign_in_button(self):
        self.click(self.__page_locator.back_to_sign_in_button)
        return self

    def wait_for_remind_pass_confirmation_popup(self):
        element_text = self.get_text(self.__page_locator.remind_pass_confirmation_popup)
        if element_text is None:
            return None
        else:
            return element_text

    def get_password_error_message(self):
        return self.get_text(self.__page_locator.password_error_message)

    def get_signin_button_text(self):
        return self.get_text(self.__page_locator.sign_in_button)
