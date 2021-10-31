import pytest
from selenium import webdriver


from config.Config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()