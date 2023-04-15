from lesson_19.page_objects.add_player_page_pack.add_player_page import AddPlayerPage
from lesson_19.page_objects.players_page_pack.players_page_locators import PlayersPageLocators
from lesson_19.utilities.web_ui.base_page import BasePage
import os
from pathlib import Path


class PlayersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__page_locator = PlayersPageLocators()
        self.__add_player_page = AddPlayerPage(self.driver)

    def download_csv_data(self):
        self.click(self.__page_locator.download_csv_button)
        home_dir = str(Path.home())
        downloads_folder_path = os.path.join(home_dir, "Downloads")
        os.chdir(downloads_folder_path)
        files = os.listdir('.')
        for file in files:
            if file.endswith('.csv'):
                return file
        # Return None only after checking all files in the directory
        return None

    # def perform_search(self):
    #     self.send_keys(self.__page_locator.search_input, value=self.__add_player_page.player_name)
    #     self.send_keys(self.__page_locator.search_input, Keys.RETURN)
