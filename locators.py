
from selenium.webdriver.common.by import By

class HomePageUrbanRoutesLocators:
    from_field_placeholder = (By.CSS_SELECTOR, "label.label[for='from']") #Verified
    from_field_input = (By.ID, "from") #Verified
    to_field_placeholder = (By.CSS_SELECTOR, "label.label[for='to']") #Verified
    to_field_input = (By.ID, "to") #Verified
    request_taxi_button = (By.CSS_SELECTOR, "button.button.round") #Verified
    select_comfort_fare =(By.CSS_SELECTOR, "img[src='/static/media/kids.075fd8d4.svg']") #Verified
    msg_to_driver_placeholder = (By.CSS_SELECTOR, "label.label[for='comment']") #Verified
    msg_to_driver_input = (By.ID, 'comment') #Verified
    check_add_towel = (By.CSS_SELECTOR, "span.slider.round") #Verified
    add_ice_cream_plus = (By.XPATH, "//div[contains(@class, 'r-counter-container')][.//div[contains(@class, 'r-counter-label') and normalize-space()='Helado']]//div[contains(@class, 'counter-plus')]") #Verified
    number_field = (By.CSS_SELECTOR, 'div.np-text') #Verified
    modal_number_field_input =(By.ID, "phone") #Verified
    modal_next_button = (By.XPATH, "//button[contains(@class, 'button') and contains(@class, 'full') and normalize-space()='Siguiente']") #Verified
    modal_code_field_placeholder = (By.CSS_SELECTOR, "label.label[for='code']") #Verified
    modal_code_field_input = (By.ID, "code") #Verified
    modal_confirm_button_code = (By.XPATH,"//button[contains(@class, 'button') and contains(@class, 'full') and normalize-space()='Confirmar']")
    payment_methods = (By.CSS_SELECTOR, 'div.pp-text') #Verified
    add_card = (By.CSS_SELECTOR, "img[src='/static/media/card.411e0152.svg']")#Verified
    card_number_field =(By.ID, 'number')#Verified
    card_code = (By.CSS_SELECTOR, "input.card-input[placeholder='12']") #Verified
    unexpected_click = (By.CSS_SELECTOR, "div.pp-buttons")#Verified
    add_card_button = (By.XPATH, "//button[contains (@class, 'button') and contains (@class, ' full') and normalize-space()='Agregar']")#Verified
    close_add_card_modal = (By.CSS_SELECTOR, "div.payment-picker.open div.modal div.section.active button.close-button.section-close")#Verified
    final_taxi_request_button = (By.CSS_SELECTOR ,'span.smart-button-main' )#Verified

    new_card = (By.XPATH, "//div[contains (@class, 'pp-title') and normalize-space()='Tarjeta']")
    added_ice_cream = (By.XPATH, "//div[contains (@class, 'counter-value') and normalize-space()='2']")