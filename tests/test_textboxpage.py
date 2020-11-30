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
        
    @mark.submit
    @mark.smoke
    def test_submitButton(self):
        actual =  self.page.submitBtn.text
        self.assertEqual(actual, 'Submit')

    @mark.label
    def test_labels(self):
        name = self.page.nameLabel.text
        self.assertEqual(name, 'Full Name')

        email = self.page.emailLabel.text
        self.assertEqual(email, 'Email')

        cAdress = self.page.currentAdrLabel.text
        self.assertEqual(cAdress, 'Current Address')

        pAdress = self.page.permanentAdrLabel.text
        self.assertEqual(pAdress, 'Permanent Address')

    @mark.input
    def test_input_fields(self):
        testName = 'Stan Alexandru'
        testEmail = 'stanalexandru@gmail.com'
        testCurrentAdr = 'Nerva Traian'
        testPermanentAdr = 'Baba Novac'

        self.page.nameInput.input_text(testName)
        self.page.emailInput.input_text(testEmail)
        self.page.currentAdrInput.input_text(testCurrentAdr)
        self.page.permanentAdrInput.input_text(testPermanentAdr)

        self.page.submitBtn.click()

        actualName = self.page.nameOutput.text
        self.assertEqual(actualName, 'Name:Stan Alexandru')

        actualEmail = self.page.emailOutput.text
        self.assertEqual(actualEmail, 'Email:stanalexandru@gmail.com')
        
        actualCurrentAdr = self.page.currentAdrOutput.text
        self.assertEqual(actualCurrentAdr, 'Current Address :Nerva Traian')

        actualPermanentAdr = self.page.permanentAdrOutput.text
        self.assertEqual(actualPermanentAdr, 'Permananet Address :Baba Novac')

        # import pdb; pdb.set_trace()

    def teardown(self):
        self.browser.quit()

