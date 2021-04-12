import unittest
from selenium import webdriver
from pytest import mark
from pytest import fixture
from pages.BaseElement import BaseElement
from pages.RadioButtonPage import RadioButtonPage
import time

@mark.radiobuttonpage
class RadioButtonPageTests(unittest.TestCase):

    def setUp(self):
        self.page = RadioButtonPage(driver=RadioButtonPageTests.browser)
        self.page.go()

    @classmethod
    def setUpClass(cls):
        super(RadioButtonPageTests, cls).setUpClass()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        super(RadioButtonPageTests, cls).tearDownClass()
        cls.browser.quit()

    @mark.label
    def test_labels(self):
        actualYes = self.page.yesLabel.text
        self.assertEqual(actualYes, 'Yes')
        
        actualImpressive = self.page.impressiveLabel.text
        self.assertEqual(actualImpressive, 'Impressive')

        actualNo = self.page.noLabel.text
        self.assertEqual(actualNo, 'No')

    @mark.smoke
    def test_pressYes(self):
        self.page.yesLabel.click()

        actual = self.page.resultText.text
        assert actual == 'Yes'


    @mark.smoke
    def test_pressImpressive(self):
        self.page.impressiveLabel.click()

        actual = self.page.resultText.text
        assert actual == 'Impressive'

    @mark.smoke
    def test_noIsDisabled(self):
        actual = self.page.noBtn.attribute('class')
        expected = 'disabled'
        assert expected in actual