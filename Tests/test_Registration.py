import time
import pytest

from Tests.Base_Test import BaseTest
from Utilities import dataProvider
from Pages.Registration_Page import Registartion_Page
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_Registration(BaseTest):

    @pytest.mark.parametrize("name, phone, email, country, city, username, password",
                             dataProvider.get_data("Login"))
    def test_Signup(self,name, phone, email, country, city, username, password):

        log.logger.info("test do signup started")
        regPage= Registartion_Page(self.driver)
        title = self.driver.title
        print(title)
# assert ("google" in title), "title doesnt match,actual title-" + title
        regPage.fill_form(name, phone, email, country, city, username, password)
        log.logger.info("test do signup successfully done")

