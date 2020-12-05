
import unittest
from selenium import webdriver
from pytest import mark
from pages.BaseElement import BaseElement
from pages.CheckBoxPage import CheckBoxPage
import time

@mark.checkboxpage
class CheckBoxPageTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.page = CheckBoxPage(driver=self.browser)
        self.page.go()
        time.sleep(3)
        
    def test_homeCheckbox(self):
        self.page.homeCheckbox.click()
        self.page.nodeBtn.click()

        expected = ['home' , 'desktop', 'notes', 'commands', 'documents', 'workspace', 
                'react', 'angular', 'veu', 'office', 'public', 'private', 'classified',
                'general', 'downloads', 'wordFile', 'excelFil']
        
        actualHome = self.page.isChecked
        self.assertEqual(actualHome, expected)

    def teardown(self):
        self.browser.quit()

