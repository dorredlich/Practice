import pytest

from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from config.Config import TestData


class Test_HomePage(BaseTest):

    @pytest.fixture(autouse=True)
    def init_data(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)

    # def test_check_main_title(self):
    #     title = self.homePage.get_main_title()
    #     assert title == TestData.DASHBOARD

    # def test_check_admin_name(self):
    #     name = self.homePage.check_admin_name()
    #     assert  name == TestData.NAME

    def test_navigate_to_document_page(self):
        self.homePage.navigate_to_document_page()

