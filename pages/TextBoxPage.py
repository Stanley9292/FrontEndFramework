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

    @property
    def nameLabel(self):
        locator = Locator(by = By.ID, value = 'userName-label')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def emailLabel(self):
        locator = Locator(by = By.ID, value = 'userEmail-label')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def currentAdrLabel(self):
        locator = Locator(by = By.ID, value = 'currentAddress-label')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def permanentAdrLabel(self):
        locator = Locator(by = By.ID, value = 'permanentAddress-label')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def nameInput(self):
        locator = Locator(by = By.ID, value = 'userName')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def emailInput(self):
        locator = Locator(by = By.ID, value = 'userEmail')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def currentAdrInput(self):
        locator = Locator(by = By.ID, value = 'currentAddress')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def permanentAdrInput(self):
        locator = Locator(by = By.ID, value = 'permanentAddress')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def nameOutput(self):
        locator = Locator(by = By.XPATH, value = '//p[@id="name"]')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def emailOutput(self):
        locator = Locator(by = By.XPATH, value = '//p[@id="email"]')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def currentAdrOutput(self):
        locator = Locator(by = By.XPATH, value = '//p[@id="currentAddress"]')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def permanentAdrOutput(self):
        locator = Locator(by = By.XPATH, value = '//p[@id="permanentAddress"]')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )