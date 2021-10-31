import pytest
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from config.Config import TestData


class Test_DocumentationPage(BaseTest):

    @pytest.fixture(autouse=True)
    def init_data(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.documentPage = self.homePage.navigate_to_document_page()

    def test_check_if_document_page(self):
        text = self.documentPage.get_document_title()
        assert text == "Sylius Documentation"

