from pages.BaseElement import BaseElement
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
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
    def elementsCliked(self):
        locator = Locator(by = By.CSS_SELECTOR, 
                        value = 'span.text-success')
        return BaseElement(
            driver=self.driver,
            locator = locator
        )

    @property
    def isChecked(self):
        names = ['home' , 'desktop', 'notes', 'commands', 'documents', 'workspace', 
                'react', 'angular', 'veu', 'office', 'public', 'private', 'classified',
                'general', 'downloads', 'wordFile', 'excelFile']
        value = '//span[contains(text(),"name")]'
        textInside = []
        for i in range(len(names)):
            val = value.replace('name', names[i])
            print(val)
            locator = Locator(by = By.XPATH, 
                            value = val)
            element =  BaseElement(
                driver=self.driver,
                locator = locator
            )
            textInside.append(element.text)
        return textInside

