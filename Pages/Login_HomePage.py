
from Pages.BasePage import BasePage
from Pages.NewCars import NewCarsPage


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def gotoNewCars(self):
        self.moveTo("newcar_XPATH")
        self.click("findnewcar_XPATH")
        return NewCarsPage(self.driver)

    def gotoCompareCars(self):
        self.moveTo("newcar_XPATH")
        self.click("comparecar_XPATH")


    def gotoUsedCars(self):
        self.moveTo("usedcar_XPATH")
        self.click("findusecar_XPATH")

