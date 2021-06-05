
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Custom_Wait:
    def __init__(self, driver):
        self.driver = driver

# explicit time-verify link present
    def verifyLinkPresence(self, text):
        self.element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.LINK_TEXT, text)))
        log.logger.info("verify link present:-" + str(text))

        # presence element
    def verifyPresenceElement(self, id):
        self.element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, id)))

    # Verify object is clickable
    def elementClickable(self, id):
        self.element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))

    # verify alert presence
    def verifyAlert(self):
        self.element = WebDriverWait(self.driver, 7, poll_frequency=5).until(EC.alert_is_present(),
        'Timed out waiting for simple alert to appear')
