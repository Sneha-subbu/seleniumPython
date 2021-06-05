
import logging
import time
import pytest

from Pages.CarBasePage import CarBasePage
from Pages.Login_HomePage import HomePage
from Tests.Base_Test import BaseTest
from Utilities import dataProvider
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_carWale(BaseTest):

    @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("inside new car section")
        home = HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(4)

    @pytest.mark.parametrize("carbrand", dataProvider.get_data("Cars"))
    def test_NewCar(self, carbrand):
        log.logger.info("selecting new car brand")
        home = HomePage(self.driver)
        carBase = CarBasePage(self.driver)
        #print(("*****car brand is****", carbrand)
        # function chaining- return object of classname in main object Page
        if carbrand == ["Hundai"]:
            home.gotoNewCars().selectHundai()
            title= self.driver.title
            assert title=="Gmail","title doesnt match,current page title is:-"+str(title)
            log.logger.info("selecting Hundai car")
            carBase.carNameandPrice()
            log.logger.info("Car and Price details for Hyundai cars")
        elif carbrand == ["BMW"]:
            home.gotoNewCars().selectBmw()
            log.logger.info("selecting car brand BMW")
            carBase.carNameandPrice()
            log.logger.info("Car and Price details for BMW cars")
        elif carbrand == ["TATA"]:
            home.gotoNewCars().selectTata()
            carBase.carNameandPrice()
        time.sleep(3)


