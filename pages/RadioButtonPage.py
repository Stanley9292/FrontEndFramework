from pages.BaseElement import BaseElement
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.Locator import Locator

class RadioButtonPage(BasePage): 

    url = 'https://demoqa.com/radio-button'

    @property
    def yesBtn(self):
        locator = Locator(by = By.CSS_SELECTOR, value = '#yesRadio')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def yesLabel(self):
        locator = Locator(by = By.CSS_SELECTOR, value = 'label[for="yesRadio"]')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def impressiveBtn(self):
        locator = Locator(by = By.ID, value = 'impressiveRadio')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def impressiveLabel(self):
        locator = Locator(by = By.CSS_SELECTOR, value = 'label[for="impressiveRadio"]')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )
        
    @property
    def noBtn(self):
        locator = Locator(by = By.XPATH, value = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[4]')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def noLabel(self):
        locator = Locator(by = By.CSS_SELECTOR, value = 'label[for="noRadio"]')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def resultText(self):
        locator = Locator(by = By.CSS_SELECTOR, value = 'span[class="text-success"]')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )
   