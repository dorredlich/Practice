from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class DocumentationPage(BasePage):
    document_title = (By.CSS_SELECTOR, "div.navbar__breadcrumbs > ul > li:nth-child(2)")

    def __init__(self, driver, handle):
        super().__init__(driver)
        self.driver.switch_to.window(handle)

    def get_document_title(self):
        return self.get_text(self.document_title)