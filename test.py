from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
import re
print('Please ensure this is all filled out correctly and country and state are CaSe SenSitive')
firstname= 'Enan'
lastname= 'Srivastava'
credit_card_number= '55555555555'
credit_card_expiration_month= '01'
credit_card_expiration_year= '18'
credit_card_crn= '123'
address1 = '2772 Squaw Valley trail'
aPT= ' '
cITY= 'Aurora'
state= 'Illinois'
zIP = '60503'
country= 'United States'
phone= '6306083688'
email= 'enan332@gmail.com'


''' firstname= input( 'First name')
lastname= input( 'Last name')
credit_card_number= input( 'Credit card(cc) #?')
credit_card_expiration_month= input( 'Cc expiration month')
credit_card_expiration_year= input( 'cc expiration year')
credit_card_crn= input( 'cc security code?')
address1 = input ('street')
aPT= input('apt,suite')
cITY= input('city')
state= input('state, ex. Illinois')
zIP = input('zip')
country= input( 'country, ex. United States')
phone= input( 'phone')
email= input( 'email') '''


url = 'https://yeezysupply.com/17655971/checkouts/ee7d92f576c0a5d78e44603605b6180c?_ga=2.32049270.912204495.1517184119-1692382194.1516591831'
z="39.5"

class checkout():
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = url
        self.verificationErrors = []

    def run(self):
        driver = self.driver
        
        driver.get(self.base_url + "/")
       
        #select = driver.find_element_by_xpath('//select[@class="PI__select PI__input js-select js-select-SIZE js-select-SIZE-static"]')

       
        ''' select1=Select(select)
        select1.select_by_visible_text(z)
        driver.find_element_by_class_name('K__button').click()
 '''
        driver.find_element_by_id("checkout_email").clear()
        driver.find_element_by_id("checkout_email").send_keys(email)
        
        driver.find_element_by_id('checkout_shipping_address_first_name').clear()
        driver.find_element_by_id('checkout_shipping_address_first_name').send_keys(firstname)
        
        driver.find_element_by_id('checkout_shipping_address_last_name').clear()
        driver.find_element_by_id('checkout_shipping_address_last_name').send_keys(lastname)
        
        driver.find_element_by_id('checkout_shipping_address_address1').clear()
        driver.find_element_by_id('checkout_shipping_address_address1').send_keys(address1)
        

        driver.find_element_by_id('checkout_shipping_address_address2').clear()
        driver.find_element_by_id('checkout_shipping_address_address2').send_keys(aPT)

        driver.find_element_by_id('checkout_shipping_address_city').clear()
        driver.find_element_by_id('checkout_shipping_address_city').send_keys(cITY)

        
        select = Select(driver.find_element_by_id('checkout_shipping_address_country'))
        # select by visible text
        select.select_by_visible_text(country)

        
        select = Select(driver.find_element_by_id('checkout_shipping_address_province'))
        # select by visible text
        select.select_by_visible_text(state)

        driver.find_element_by_id('checkout_shipping_address_zip').clear()
        driver.find_element_by_id('checkout_shipping_address_zip').send_keys(zIP)

        driver.find_element_by_id('checkout_shipping_address_phone').clear()
        driver.find_element_by_id('checkout_shipping_address_phone').send_keys(phone)

        
        

        driver.find_element_by_xpath('//span[@class="btn__content"]').click()
        driver.find_element_by_xpath('//span[@class="btn__content"]').click()
        




        time.sleep(1)
        driver.switch_to.frame(0)

        #driver.switch_to_frame(iframe)
        #driver.find_elements_by_tag_name('iframe')[1]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        
        
        driver.find_element_by_id('number').clear()
        driver.find_element_by_id("number").send_keys("1233312")

        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
       
        #driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="card-fields-name-3v80qxylts'))
        driver.switch_to_default_content()
        driver.switch_to.frame(1)

        xp1 = '(//*[@autocomplete="cc-name"])'
        driver.find_element_by_xpath(xp1).clear()
        driver.find_element_by_xpath(xp1).send_keys("enan")

        ''' driver.find_element_by_id('name')[1].clear()
        driver.find_element_by_id('name')[1].send_keys("enan") '''
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=2 | ]]
        driver.switch_to_default_content()
        driver.switch_to.frame(2)
        driver.find_element_by_id("expiry").clear()
        driver.find_element_by_id("expiry").send_keys("12 / 12")

        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]frame id has unexpected type
        
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=3 | ]]
        driver.switch_to_default_content()
        driver.switch_to.frame(3)
        driver.find_element_by_id("verification_value").clear()
        driver.find_element_by_id("verification_value").send_keys("123")
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.switch_to_default_content()
        driver.find_element_by_id("checkout_different_billing_address_false").click()
        driver.find_element_by_css_selector("button[name=\"button\"] > span.btn__content").click()
    
x = checkout()
x.setUp()
x.run()
