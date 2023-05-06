from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.webdriver import WebDriver as SafariDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


__CHROME = 1
__FIREFOX = 2
__SAFARI = 3

# will be improved later, used to run tests 'headless', not opening browser
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')  # to run tests in CI


def driver_factory(driver_id: int):
    if int(driver_id) == __CHROME:
        return Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    elif int(driver_id) == __FIREFOX:
        return Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif int(driver_id) == __SAFARI:
        return SafariDriver()
    else:
        return Chrome(service=ChromeService(ChromeDriverManager().install()))

