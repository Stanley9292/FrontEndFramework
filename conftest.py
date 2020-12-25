from selenium import webdriver
from pytest import fixture


@fixture(scope='session')
def chrome_browser():
     browser = webdriver.Chrome()
     yield browser