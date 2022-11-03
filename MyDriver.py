import time
from typing import Optional

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.remote.webelement import WebElement

class MyDriver(Firefox):
    def element_exist(self,by,value):
        try:
            self.find_element(by=by,value=value)
        except NoSuchElementException:
            return False

        return True

    def wait_until_element_will_be_visible(self, by, value, waitTime=5):
        t = time.time()
        while not self.element_exist(by, value):

            if time.time() - t > waitTime:
                raise TimeoutError("element not visible since " + str(waitTime) + "s")

    # def find_MyWebElement(self, by=By.ID, value=None) -> WebElement:
    #     # element -> WebElement
    #     element = self.find_element(by, value)
    #
    #     element = MyWebElement(element)
    #
    #     return element
