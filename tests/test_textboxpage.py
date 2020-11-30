import unittest
from selenium import webdriver
from pytest import mark
from pages.BaseElement import BaseElement
from pages.TextBoxPage import TextBoxPage
import time

@mark.textboxpage
class TextBoxPageTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.page = TextBoxPage(driver=self.browser)
        self.page.go()
        time.sleep(3)

    @mark.submit
    @mark.smoke
    def test_submitButton(self):
        actual =  self.page.submitBtn.text
        self.assertEqual(actual, 'Submit')

        self.page.submitBtn.find()
        self.page.submitBtn.click()

    def test_labels(self):
        pass

    def teardown(self):
        self.browser.quit()

