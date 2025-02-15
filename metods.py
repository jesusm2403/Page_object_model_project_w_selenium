import data
from retrieve_code import retrieve_phone_code
from locators import HomePageUrbanRoutesLocators
import time

class HomePageUrbanRoutesMethods:
    def __init__(self, driver):
        self.driver = driver

       #Metodos para el TestCase #1
    def make_click_set_from(self): #Verificado
        self.driver.find_element(*HomePageUrbanRoutesLocators.from_field_placeholder).click()
    def set_from(self):#Verificado
        self.driver.find_element(*HomePageUrbanRoutesLocators.from_field_input).send_keys(data.address_from)
    def make_click_set_to(self):#Verificado
        self.driver.find_element(*HomePageUrbanRoutesLocators.to_field_placeholder).click()
    def set_to(self):#Verificado
        self.driver.find_element(*HomePageUrbanRoutesLocators.to_field_input).send_keys(data.address_to)

    def make_click_request_taxi_button(self): #Verificado
        self.driver.find_element(*HomePageUrbanRoutesLocators.request_taxi_button).click()
    #Metodo para el TestCase #2
    def set_comfort_fare(self): #Verificado
        self.driver.find_element(*HomePageUrbanRoutesLocators.select_comfort_fare).click()


    #Metodos para el TestCase #3
    def make_click_phone_number_field(self): #Verificado
        self.driver.find_element(*HomePageUrbanRoutesLocators.number_field).click()
    def write_phone_number_field_modal(self): #Verificado
        self.driver.find_element(*HomePageUrbanRoutesLocators.modal_number_field_input).send_keys(data.phone_number)
    def make_click_next_button_phone_number_modal(self): #verificado
        self.driver.find_element(*HomePageUrbanRoutesLocators.modal_next_button).click()
    def make_click_insert_code_placeholder(self): #Verificado
        self.driver.find_element(*HomePageUrbanRoutesLocators.modal_code_field_placeholder).click()
    def write_phone_code_input(self):
        code = retrieve_phone_code(driver=self.driver)
        self.driver.find_element(*HomePageUrbanRoutesLocators.modal_code_field_input).send_keys(code)
    def make_click_confirm_button(self):
        self.driver.find_element(*HomePageUrbanRoutesLocators.modal_confirm_button_code).click()

    #Metodos para el TestCase #4
    def make_click_payment_methods(self):#verificado
        self.driver.find_element(*HomePageUrbanRoutesLocators.payment_methods).click()
    def make_click_add_card_modal(self): #verificado
        self.driver.find_element(*HomePageUrbanRoutesLocators.add_card).click()

    def make_click_and_write_card_number_field(self):
        self.driver.find_element(*HomePageUrbanRoutesLocators.card_number_field).click()
        self.driver.find_element(*HomePageUrbanRoutesLocators.card_number_field).send_keys(data.card_number)
    def make_click_card_code_field(self):
        self.driver.find_element(*HomePageUrbanRoutesLocators.card_code).click()
    def write_card_code_field(self):
        self.driver.find_element(*HomePageUrbanRoutesLocators.card_code).send_keys(data.card_code)
    def make_an_unexpected_click(self):
        self.driver.find_element(*HomePageUrbanRoutesLocators.unexpected_click).click()
    def make_click_add_card_button_add_card(self):
        self.driver.find_element(*HomePageUrbanRoutesLocators.add_card_button).click()
    def make_click_close_modal_add_card(self):
        self.driver.find_element(*HomePageUrbanRoutesLocators.close_add_card_modal).click()

    #Metodo para el TestCase #5 #Funcionales
    def make_click_message_to_driver_placeholder(self):
        self.driver.find_element(*HomePageUrbanRoutesLocators.msg_to_driver_placeholder).click()
    def write_message_to_driver_input(self):
        self.driver.find_element(*HomePageUrbanRoutesLocators.msg_to_driver_input).send_keys(data.message_for_driver)

    #Metodo para el Testcase #6
    def set_towel_on(self):
        self.driver.find_element(*HomePageUrbanRoutesLocators.check_add_towel).click()

    #Metodo para el TestCase #7
    def add_ice_cream(self):
        self.driver.find_element(*HomePageUrbanRoutesLocators.add_ice_cream_plus).click()
        self.driver.find_element(*HomePageUrbanRoutesLocators.add_ice_cream_plus).click()

    #Metodo para el Testcase #8
    def final_taxi_request_button(self):
        self.driver.find_element(*HomePageUrbanRoutesLocators.final_taxi_request_button).click()

    def wait_seconds(self):
        time.sleep(40)