from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator


        self.web_element = None
        self.find()
    
    def find(self):
        
        element = WebDriverWait(
            self.driver, 10).until(EC.visibility_of_element_located(
                locator=self.locator
            ))
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(
            self.driver, 10).until(EC.element_to_be_clickable(
                locator=self.locator
            ))
        element.click()
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    def attribute(self, atr_name):
        self.web_element.get_attribute(atr_name)
        return None