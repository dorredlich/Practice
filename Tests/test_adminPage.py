import pytest

from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from config.Config import TestData


class Test_AdminPage(BaseTest):

    @pytest.fixture(autouse=True)
    def init_data(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.adminPage = self.homePage.move_admin_page()

    def test_check_if_in_admin_page(self):
        text = self.adminPage.get_admin_main_title()
        assert text == TestData.ADMIN

    def test_check_select(self):
        state_name = self.adminPage.select_state_by_number(10)
        assert state_name == "Amharic"