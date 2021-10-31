from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from config.Config import TestData


class LoginPage(BasePage):
    user_name = (By.ID, "_username")
    password = (By.ID, "_password")
    login_button = (By.CSS_SELECTOR, ".ui.fluid.large.primary.submit.button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_login(self, userName, passw):
        self.send_keys(self.user_name, userName)
        self.send_keys(self.password, passw)
        self.click(self.login_button)