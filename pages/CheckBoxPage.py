from pages.BaseElement import BaseElement
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.Locator import Locator

class CheckBoxPage(BasePage): 

    url = 'https://demoqa.com/checkbox'

    @property
    def nodeBtn(self):
        locator = Locator(by = By.XPATH, 
                        value = '//*[@id="tree-node"]/ol/li/span/button')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def nodeDesktopBtn(self):
        locator = Locator(by = By.XPATH, 
                        value = '//*[@id="tree-node"]/ol/li/ol/li[1]/span/button')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def nodeDownloadsBtn(self):
        locator = Locator(by = By.XPATH, 
                        value = '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    # "input[id='tree-node-home'][type='checkbox']"
    @property
    def homeCheckbox(self):
        locator = Locator(by = By.CSS_SELECTOR, 
                        value = "label[for='tree-node-home']")
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def desktopCheckbox(self):
        locator = Locator(by = By.CSS_SELECTOR, 
                        value = "label[for='tree-node-desktop']")
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def notesCheckbox(self):
        locator = Locator(by = By.CSS_SELECTOR, 
                        value = "label[for='tree-node-notes']")
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def wordFileCheckbox(self):
        locator = Locator(by = By.CSS_SELECTOR, 
                        value = "label[for='tree-node-wordFile']")
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def documentsCheckbox(self):
        locator = Locator(by = By.CSS_SELECTOR, 
                        value = "label[for='tree-node-documents']")
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def elementsCliked(self):
        locator = Locator(by = By.CSS_SELECTOR, 
                        value = 'span.text-success')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    def isChecked(self, expected_list):
        value = '//span[contains(text(),"name")]'
        textInside = []
        for i in range(len(expected_list)):
            val = value.replace('name', expected_list[i])
            try:
                locator = Locator(by = By.XPATH, 
                                value = val)
                element =  BaseElement(
                    driver=self.driver,
                    locator = locator
                )
                textInside.append(element.text)
            except: TimeoutException
        return textInside

