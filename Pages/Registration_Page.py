from Pages.BasePage import BasePage
from Utilities import configReader

class Registartion_Page(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    def fill_form(self,name, phone, email, country, city, username, password):
        self.TypeInputvalue("name_CSS", name)
        self.TypeInputvalue("phone_XPATH", phone)
        self.TypeInputvalue("email_XPATH", email)
        self.select("country_XPATH", country)
        self.TypeInputvalue("city_XPATH",city)
        self.TypeInputvalue("username_XPATH", username)
        self.TypeInputvalue("password_XPATH", password)
        self.click("submit_XPATH")


