
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
        
    @mark.homeCheckbox
    def test_homeCheckbox(self):
        self.page.homeCheckbox.click()
        self.page.nodeBtn.click()

        expected = ['home' , 'desktop', 'notes', 'commands', 'documents', 'workspace', 
                'react', 'angular', 'veu', 'office', 'public', 'private', 'classified',
                'general', 'downloads', 'wordFile', 'excelFile']
        actual = self.page.isChecked
        self.assertEqual(actual, expected)

    @mark.selectFolder
    def test_selectFolder(self):
        self.page.nodeBtn.click()
        self.page.desktopCheckbox.click()

        expected = ['desktop', 'notes', 'commands']
        actual = self.page.isChecked
        self.assertEqual(actual, expected)

    @mark.selectFile
    def test_selectFile(self):
        self.page.nodeBtn.click()
        self.page.nodeDesktopBtn.click()
        self.page.notesCheckbox.click()

        expected = ['notes']
        actual = self.page.isChecked
        self.assertEqual(actual, expected)

    @mark.selectMultipleFolders
    def test_selectMultipleFolders(self):
        self.page.nodeBtn.click()
        self.page.desktopCheckbox.click()
        self.page.documentsCheckbox.click()

        expected = ['desktop', 'notes', 'commands', 'documents', 'workspace', 'react', 
                'angular', 'veu', 'office', 'public', 'private', 'classified', 'general']
        actual = self.page.isChecked
        self.assertEqual(actual, expected)

    @mark.selectMultipleFiles
    def test_selectMultipleFiles(self):
        self.page.nodeBtn.click()
        self.page.nodeDesktopBtn.click()
        self.page.notesCheckbox.click()
        self.page.nodeDownloadsBtn.click()
        self.page.wordFileCheckbox.click()

        expected = ['notes', 'wordFile']
        actual = self.page.isChecked
        self.assertEqual(actual, expected)


    def teardown(self):
        self.browser.quit()

