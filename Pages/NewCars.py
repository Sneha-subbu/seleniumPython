from Pages.BasePage import BasePage

class NewCarsPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    def selectHundai(self):
        self.click("hundai_XPATH")

    def selectTata(self):
        self.click("tata_XPATH")

    def selectBmw(self):
        self.click("bmw_XPATH")