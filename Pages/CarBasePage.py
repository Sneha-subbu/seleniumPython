import logging
from Pages.BasePage import BasePage
from Utilities import configReader
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

class CarBasePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def carNameandPrice(self):
        carPrice = self.driver.find_elements_by_xpath(configReader.readConfig("locators","carPrice_XPATH"))
        carTitle = self.driver.find_elements_by_xpath(configReader.readConfig("locators","carTitle_XPATH"))
        for i in range (1,len(carPrice)):
            print(("Car Price are:-" + carPrice[i].text + "*****************"+"Car title are:" + carTitle[i].text).encode('utf8'))
            log.logger.info("Car Price are:-" + carPrice[i].text + "*****************"+"Car title are:" + carTitle[i].text)