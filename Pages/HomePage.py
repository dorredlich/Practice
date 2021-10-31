from selenium.webdriver.common.by import By

from Pages.AdminPage import AdminPage
from Pages.BasePage import BasePage


class HomePage(BasePage):
    dashboard = (By.CSS_SELECTOR, "#content > div:nth-child(1) > div.twelve.wide.column > h1 > div")
    admin_name = (By.CSS_SELECTOR, "body > div.ui.borderless.fixed.menu > div:nth-child(8) > span")
    my_account_button = (By.CSS_SELECTOR, "body > div.ui.borderless.fixed.menu > div.ui.floated.simple.dropdown.item.active.visible > div > a:nth-child(1)")

    def __init__(self, driver):
        super().__init__(driver)

    def get_main_title(self):
        if self.is_visible(self.dashboard):
            return self.get_text(self.dashboard)

    def check_admin_name(self):
        return self.get_text(self.admin_name)

    def move_admin_page(self):
        self.click(self.admin_name)
        self.click(self.my_account_button)
        return AdminPage(self.driver)