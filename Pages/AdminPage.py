from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class AdminPage(BasePage):
    admin_title = (By.CSS_SELECTOR, "#content > div.ui.stackable.two.column.grid > div:nth-child(1) > h1 > div")


    def __init__(self, driver):
        super().__init__(driver)

    def get_admin_main_title(self):
        if self.is_visible(self.admin_title):
            return self.get_text(self.admin_title)