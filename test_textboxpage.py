from selenium import webdriver
from pages.BaseElement import BaseElement
from pages.TextBoxPage import TextBoxPage

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
    assert page.submitBtn.text == 'Submit'
    page.submitBtn.click()
    browser.quit()

