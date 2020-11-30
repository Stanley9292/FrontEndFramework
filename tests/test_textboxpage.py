from selenium import webdriver
# import sys 
# sys.path.append('../')
# sys.path.insert(1, 'workspace\FrontEndFramework\pages')
from pages.BaseElement import BaseElement
from pages.TextBoxPage import TextBoxPage
import time

# Test setup
browser = webdriver.Chrome()


# # 
# page = TextBoxPage(driver=browser)
# page.go() 
# assert page.submitBtn.text == 'Submit'
# page.submitBtn.click()
# browser.quit()

def test_submitButton():
    page = TextBoxPage(driver=browser)
    page.go() 
    time.sleep(3)
    # assert page.submitBtn.text == 'Submit'
    page.submitBtn.find()
    page.submitBtn.click()
    # browser.quit()

