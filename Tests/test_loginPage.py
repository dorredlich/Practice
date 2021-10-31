import pytest
from Tests.BaseTest import BaseTest
from config.Config import TestData
from Pages.LoginPage import LoginPage


class Test_Login(BaseTest):

    # @pytest.fixture(autouse=True)
    # def init_data(self):
    #     self.loginPage = LoginPage(self.driver)

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)