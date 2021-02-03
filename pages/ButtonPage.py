from pages.BaseElement import BaseElement
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.Locator import Locator

class ButtonPage(BasePage): 

    url = 'https://demoqa.com/buttons'

    @property
    def doubleClickBtn(self):
        locator = Locator(by = By.XPATH, 
                        value = '//*[@id="doubleClickBtn"]')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def doubleClickMsg(self):
        locator = Locator(by = By.CSS_SELECTOR, 
                        value = '#doubleClickMessage')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def rightClickBtn(self):
        locator = Locator(by = By.ID, 
                        value = 'rightClickBtn')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def rightClickMsg(self):
        locator = Locator(by = By.CSS_SELECTOR, 
                        value = '#rightClickMessage')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def clickMeBtn(self):
        locator = Locator(by = By.XPATH, 
                        value = '/html/body/div/div/div/div[2]/div[2]/div[1]/div[3]/button')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def clickMeMsg(self):
        locator = Locator(by = By.CSS_SELECTOR, 
                        value = '#dynamicClickMessage')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

