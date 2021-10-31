from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class AdminPage(BasePage):
    admin_title = (By.CSS_SELECTOR, "#content > div.ui.stackable.two.column.grid > div:nth-child(1) > h1 > div")
    select_state = (By.CSS_SELECTOR, "#sylius_admin_user_localeCode")

    def __init__(self, driver):
        super().__init__(driver)

    def get_admin_main_title(self):
        if self.is_visible(self.admin_title):
            return self.get_text(self.admin_title)

    def select_state_by_number(self, number):
        state_options = self.select_element(self.select_state)
        for option_index in range(len(state_options.options)):
            if option_index == number:
                state_options.select_by_index(number)
                return state_options.first_selected_option.text
