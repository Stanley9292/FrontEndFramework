from selenium import webdriver
from ..pages import BaseElement
from ..pages import TextBoxPage

# Test setup
browser = webdriver.Chrome()


# 
page = TextBoxPage(driver=browser)
page.go() 
assert page.submitBtn.text == 'Submitted'
page.submitBtn.click()
browser.quit()