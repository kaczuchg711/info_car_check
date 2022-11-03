from selenium.webdriver.remote.webelement import WebElement


class MyWebElement(WebElement):
    pass
    def __init__(self, parent, id_):
        super().__init__(parent, id_)

