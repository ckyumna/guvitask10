import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def get_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()

