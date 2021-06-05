from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Utilities import configReader
import logging

from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

# key driven approach we will follow here and will replace all common used line of codes
# (will define action on this page.)

# click button

    def click(self, key):
        if str(key).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configReader.readConfig("locators", key)).click()
        elif str(key).endswith("_CSS"):
            self.driver.find_element_by_css_selector(configReader.readConfig("locators", key)).click()
        elif str(key).endswith("_ID"):
            self.driver.find_element_by_id(configReader.readConfig("locators", key)).click()
        log.logger.info("element clicking on :-" + str(key))

# Enter values in text box

    def TypeInputvalue(self, key, value):
        if str(key).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configReader.readConfig("locators", key)).send_keys(value)
        elif str(key).endswith("_CSS"):
            self.driver.find_element_by_css_selector(configReader.readConfig("locators", key)).send_keys(value)
        elif str(key).endswith("_ID"):
            self.driver.find_element_by_id(configReader.readConfig("locators", key)).send_keys(value)

        log.logger.info("input value in field :-" + str(key)+"values entered as--" + str(value))

# select drop down

    def select(self, locator, value):
        global dropdown
        if str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element_by_xpath(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            dropdown = self.driver.find_element_by_id(configReader.readConfig("locators", locator))

        select = Select(dropdown)
        select.select_by_visible_text(value)

        log.logger.info("selecting value in field :-" + str(locator) + "values selected--" + str(value))

# Mouseover Action

    def moveTo(self,locator):
        global element
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element_by_xpath(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element_by_id(configReader.readConfig("locators", locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        log.logger.info("moving to element :-" + str(locator))




# Js script
    def js_scroll_up(self):
        self.driver.execute_script('window.scrollBy(0,-300)')
        log.logger.info('Scrolling Up')

    def js_scroll_down(self):
        self.driver.execute_script('window.scrollBy(0,300)')
        log.logger.info('Scrolling Down')

    def js_scroll_right(self):
        self.driver.execute_script('window.scrollBy(300,0)')
        log.logger.info('Scrolling Right')

    def js_scroll_left(self):
        self.driver.execute_script('window.scrollBy(-300,0)')
        log.logger.info('Scrolling Left')

# Keyboard input

    def send_keyboard_input(self, key):
        action = ActionChains(self.driver)
        if key.upper() == 'ARROW_DOWN':
            action.send_keys(Keys.ARROW_DOWN).perform()
            log.logger.info('Performed keyboard action Arrow Down')
        elif key.upper() == 'ARROW_UP':
            action.send_keys(Keys.ARROW_UP).perform()
            log.logger.info('Performed keyboard action Arrow Up')
        elif key.upper() == 'BACK_SPACE':
            action.send_keys(Keys.BACK_SPACE).perform()
            log.logger.info('Performed keyboard action Back Space')
        elif key.upper() == 'ESCAPE':
            action.send_keys(Keys.ESCAPE).perform()
            log.logger.info('Performed keyboard action Escape')
        elif key.upper() == 'TAB':
            action.send_keys(Keys.TAB).perform()
            log.logger.info('Performed keyboard action Tab')
        elif key.upper() == 'ENTER':
            action.send_keys(Keys.ENTER).perform()
            log.logger.info('Performed keyboard action Enter')

# scripts for child window and frame
    def accept_alert(self, timeout=0):
        alert = Alert(self.driver)
        alert.accept()
        log.logger.info('Alert Accepted')


    def dismiss_alert(self, timeout=0):
        alert = Alert(self.driver)
        alert.dismiss()
        log.logger.info('Alert Dismissed')


    def get_alert_text(self, timeout=0):
        alert = Alert(self.driver)
        return alert.text.strip() if alert.text.strip() else None

    def switch_to_window(self, window_index):
        if window_index < len(self.driver.window_handles):
            self.driver.switch_to.window(self.driver.window_handles[window_index])
            log.logger.info('Switched to window index: ' + window_index)
        else:
            raise NoSuchWindowException(f'Window index :{window_index} does not exist')

    def switch_to_parent_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        log.logger.info('Switched to Parent window')

    def close_window(self, window_index):
        if window_index < len(self.driver.window_handles):
            self.driver.switch_to.window(self.driver.window_handles[window_index])
            self.driver.close()
            log.logger.info('Closed window index:' + window_index)
        else:
            raise NoSuchWindowException(f'Window index :{window_index} does not exist')

    def close_all_child_window(self):
        handles = self.driver.window_handles
        for index in range(1, len(handles)):
            self.driver.switch_to.window(handles[index])
            self.driver.close()
            log.logger.info('Closed all child windows')

# click element using Js page-when iframe,java script occur
    def js_click_element(self, key):
        global element
        if str(key).endswith("_XPATH"):
            element = self.driver.find_element_by_xpath(configReader.readConfig("locators", key))
        elif str(key).endswith("_CSS"):
            element = self.driver.find_element_by_css_selector(configReader.readConfig("locators", key))
        elif str(key).endswith("_ID"):
            element = self.driver.find_element_by_id(configReader.readConfig("locators", key))
        self.driver.execute_script('arguments[0].click()', element)
        log.logger.info('Performed JS click on ' + str(key))

# edit box text
    def js_enter_text(self, key ):
        global element
        if str(key).endswith("_XPATH"):
            element = self.driver.find_elementby_xpath(configReader.readConfig("locators", key))
        elif str(key).endswith("_CSS"):
            element = self.driver.find_element_by_css_selector(configReader.readConfig("locators", key))
        elif str(key).endswith("_ID"):
            element = self.driver.find_element_by_css_id(configReader.readConfig("locators", key))
        self.driver.execute_script('arguments[0].value=arguments[1]', element)
        log.logger.info('Performed JS edit on ' + str(key))