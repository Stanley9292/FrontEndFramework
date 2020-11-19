from pages.BaseElement import BaseElement
from selenium.webdriver.common.by import By

class TextBoxPage: 
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://demoqa.com/text-box'

    def go(self):
        self.driver.get(self.url)

    @property
    def submitBtn(self):
        locator = (By.ID, 'submit')
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )