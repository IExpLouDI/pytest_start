from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def browser():
	driver = webdriver.Chrome()
	yield driver
	driver.quit()
