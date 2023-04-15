import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 10)

    def wait_until_element_located(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def wait_until_to_be_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def wait_for_url(self, URL: str):
        return self.__wait.until(EC.url_contains(URL))

    # def _send_keys(self, locator, value):
    #     self.driver.find_element(locator, value).send_keys()

    def click(self, locator):
        self.wait_until_to_be_clickable(locator).click()

    # def click(self, locator):  # click moving mouse pointer
    #     element = self.wait_until_to_be_clickable(locator)
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(element)
    #     actions.click()
    #     actions.perform()

    # def _click(self, locator):
    #     self.driver.find_element(locator).click()

    def click_via_js(self, locator):
        self.driver.execute_script('arguments[0].click();', self.wait_until_to_be_clickable(locator))

    def send_keys(self, locator, value, is_clear=True):
        element = self.wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def send_keys_js(self, locator, value):
        element = self.wait_until_element_located(locator)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, value)

    def clear_fields_js(self, locator):
        element = self.wait_until_element_located(locator)
        self.driver.execute_script("arguments[0].value = '';", element)

    def get_text(self, locator):
        element = self.wait_until_element_located(locator)
        return element.text

    def vertical_scroll_page(self, y: int):
        self.driver.execute_script(f'window.scrollBy(0,{y})')

    def scroll_to_element(self, locator):
        max_retries = 10
        _try = 0
        while _try != max_retries:
            try:
                element = self.wait_until_element_located(locator)
                return element
            except Exception:
                self.vertical_scroll_page(100)
                _try += 1
        raise NoSuchElementException(str(locator))

    def is_element_visible(self, locator):
        element = self.wait_until_element_located(locator)
        return element.is_visible()

    def select_item_from_dropdown(self, value, locator):
        element = self.__wait.until(EC.visibility_of_element_located(locator))
        sel = Select(element)
        sel.select_by_value(value)

    def find_element(self, method, element):
        try:
            return self.driver.find_element(method, element)
        except NoSuchElementException:
            # If element is not located
            print(f"Element {element} not found")
            return None

    def wait_until_to_be_disabled(self, element):
        self.__wait.until(EC.element_to_be_clickable((By.XPATH, element.get_attribute('disabled'))))

    def get_title(self):
        return self.driver.title

    def clear_all_fields_js(self):
        js_script = "document.querySelectorAll('input').forEach(input => input.value = '');"
        self.driver.execute_script(js_script)

    def reset_form_js(self, locator):
        form_element = self.wait_until_element_located(locator)
        self.driver.execute_script("arguments[0].reset();", form_element)

    def clear_input_field(self, element):
        # Click on the input field to make it active
        element.click()

        # Create an ActionChains object
        actions = ActionChains(self.driver)

        # Send a series of BACKSPACE keys to clear the field
        actions.send_keys(Keys.BACKSPACE * len(element.get_attribute("value")))

        # Perform the actions
        actions.perform()
