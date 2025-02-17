from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators
from locators import HomePageUrbanRoutesLocators
import data
from selenium import webdriver
from metods import HomePageUrbanRoutesMethods


class TestUrbanRoutes:

    driver = None
    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    #TestCase Number #1
    def test_directions_checks(self):
        self.driver.get(data.urban_routes_url)
        home_page_methods = HomePageUrbanRoutesMethods(self.driver)
        home_page_methods.make_click_set_from()
        home_page_methods.set_from()
        home_page_methods.make_click_set_to()
        home_page_methods.set_to()
        from_field = self.driver.find_element(*HomePageUrbanRoutesLocators.from_field_input)
        to_field = self.driver.find_element(*HomePageUrbanRoutesLocators.to_field_input)
        from_expected = data.address_from
        to_expected = data.address_to
        assert from_field.get_attribute('value') == from_expected
        assert to_field.get_attribute('value') == to_expected
    def test_select_comfort_fare(self):
        home_page_methods = HomePageUrbanRoutesMethods(self.driver)
        home_page_methods.make_click_request_taxi_button()
        home_page_methods.set_comfort_fare()
        comfort_fare_class = self.driver.find_element(*HomePageUrbanRoutesLocators.select_comfort_fare)
        assert "active" in comfort_fare_class.get_attribute("class")
    def test_add_number_phone(self):
        home_page_methods = HomePageUrbanRoutesMethods(self.driver)
        home_page_methods.make_click_phone_number_field()
        home_page_methods.write_phone_number_field_modal()
        home_page_methods.make_click_next_button_phone_number_modal()
        home_page_methods.make_click_insert_code_placeholder()
        home_page_methods.write_phone_code_input()
        home_page_methods.make_click_confirm_button()
        phone_number_field = self.driver.find_element(*HomePageUrbanRoutesLocators.modal_number_field_input)
        phone_number_expected = data.phone_number
        assert phone_number_field.get_attribute('value') == phone_number_expected
    def test_add_payment_method_card(self):
        home_page_methods = HomePageUrbanRoutesMethods(self.driver)
        home_page_methods.make_click_payment_methods()
        home_page_methods.make_click_add_card_modal()
        home_page_methods.make_click_and_write_card_number_field()
        home_page_methods.make_click_card_code_field()
        home_page_methods.write_card_code_field()
        home_page_methods.make_an_unexpected_click()
        home_page_methods.make_click_add_card_button_add_card()
        home_page_methods.make_click_close_modal_add_card()

        added_new_card = self.driver.find_element(*HomePageUrbanRoutesLocators.new_card)
        added_card_expected = "Tarjeta"
        assert added_new_card.get_attribute('value') == added_card_expected
    def test_add_msg_to_driver(self):
        home_page_methods = HomePageUrbanRoutesMethods(self.driver)
        home_page_methods.make_click_message_to_driver_placeholder()
        home_page_methods.write_message_to_driver_input()
        msg_to_driver = self.driver.find_element(*HomePageUrbanRoutesLocators.msg_to_driver_input)
        msg_to_driver_expected = data.message_for_driver
        assert msg_to_driver.get_attribute('value') == msg_to_driver_expected
    def test_add_towel(self):
        home_page_methods = HomePageUrbanRoutesMethods(self.driver)
        home_page_methods.set_towel_on()
        add_towel_class = self.driver.find_element(*HomePageUrbanRoutesLocators.check_add_towel)
        assert add_towel_class.is_selected()
    def test_add_ice_cream(self):
        home_page_methods = HomePageUrbanRoutesMethods(self.driver)
        home_page_methods.add_ice_cream()
        added_ice_cream = self.driver.find_element(*HomePageUrbanRoutesLocators.added_ice_cream)
        amount_added_ice_cream = data.amount_added_ice_cream
        assert added_ice_cream.get_attribute('value') == amount_added_ice_cream
    def test_request_taxi(self):
        home_page_methods = HomePageUrbanRoutesMethods(self.driver)
        home_page_methods.final_taxi_request_button()
        WebDriverWait(self.driver, 40).until(expected_conditions.presence_of_element_located(locators.HomePageUrbanRoutesLocators.wait_for))

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


