import unittest
from selenium import webdriver
from pytest import mark
from pytest import fixture
from pages.BaseElement import BaseElement
from pages.ButtonPage import ButtonPage
import time
import pdb

@mark.buttonpage
class ButtonPageTests(unittest.TestCase):

    def setUp(self):
        self.page = ButtonPage(driver=ButtonPageTests.browser)
        self.page.go()

    @classmethod
    def setUpClass(cls):
        super(ButtonPageTests, cls).setUpClass()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        super(ButtonPageTests, cls).tearDownClass()
        cls.browser.quit()

    
    # def test_double_click(self):
    #     # self.page.doubleClickBtn.double_click
    #     # self.page.doubleClickBtn.double_click
    #     # time.sleep(4)

   
    # def test_right_click(self):
    #     pdb.set_trace()
    #     self.page.rightClickBtn.click()
    #     self.page.rightClickBtn.right_click
    #     time.sleep(4)

   
    def test_click_me(self):
        self.page.clickMeBtn.click()

        actual = self.page.clickMeMsg.text
        self.assertEqual(actual, 'You have done a dynamic click')
    