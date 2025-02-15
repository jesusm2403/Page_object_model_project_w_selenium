
from selenium.webdriver.common.by import By

class HomePageUrbanRoutesLocators:
    from_field_placeholder = (By.CSS_SELECTOR, "label.label[for='from']") #Verificado
    from_field_input = (By.ID, "from") #Verificado
    to_field_placeholder = (By.CSS_SELECTOR, "label.label[for='to']") #Verificado
    to_field_input = (By.ID, "to") #Verificado
    request_taxi_button = (By.CSS_SELECTOR, "button.button.round") #Verificado
    select_comfort_fare =(By.CSS_SELECTOR, "img[src='/static/media/kids.075fd8d4.svg']") #Verificado
    msg_to_driver_placeholder = (By.CSS_SELECTOR, "label.label[for='comment']") #Verificado
    msg_to_driver_input = (By.ID, 'comment') #Verificado
    check_add_towel = (By.CSS_SELECTOR, "span.slider.round") #Verificado
    add_ice_cream_plus = (By.XPATH, "//div[contains(@class, 'r-counter-container')][.//div[contains(@class, 'r-counter-label') and normalize-space()='Helado']]//div[contains(@class, 'counter-plus')]") #Verificado
    number_field = (By.CSS_SELECTOR, 'div.np-text') #verificado
    modal_number_field_input =(By.ID, "phone") #verificado
    modal_next_button = (By.XPATH, "//button[contains(@class, 'button') and contains(@class, 'full') and normalize-space()='Siguiente']") #verificado
    modal_code_field_placeholder = (By.CSS_SELECTOR, "label.label[for='code']") #verificado
    modal_code_field_input = (By.ID, "code") #verificado
    modal_confirm_button_code = (By.XPATH,"//button[contains(@class, 'button') and contains(@class, 'full') and normalize-space()='Confirmar']")
    payment_methods = (By.CSS_SELECTOR, 'div.pp-text') #verificado
    add_card = (By.CSS_SELECTOR, "img[src='/static/media/card.411e0152.svg']")#verificado
    card_number_field =(By.ID, 'number')#verificado
    card_code = (By.CSS_SELECTOR, "input.card-input[placeholder='12']") #verificado
    unexpected_click = (By.CSS_SELECTOR, "div.pp-buttons")#verificado
    add_card_button = (By.XPATH, "//button[contains (@class, 'button') and contains (@class, ' full') and normalize-space()='Agregar']")#verificado
    close_add_card_modal = (By.CSS_SELECTOR, "div.payment-picker.open div.modal div.section.active button.close-button.section-close")#verificado
    final_taxi_request_button = (By.CSS_SELECTOR ,'span.smart-button-main' )

