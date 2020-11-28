from pages.BaseElement import BaseElement
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.Locator import Locator

class TextBoxPage(BasePage): 

    url = 'https://demoqa.com/text-box'

    @property
    def submitBtn(self):
        locator = Locator(by = By.ID, value = 'submit')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )