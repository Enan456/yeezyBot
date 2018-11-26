# imports, imports galore, yay
import json
import time
import httplib2
import lxml
import requests
from random import randint
from bs4 import SoupStrainer
from bs4 import BeautifulSoup
import configparser
import re
from lxml import html
import requests
import time
import datetime
import webbrowser
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
links = []
url = 'http://yeezysupply.com'
url1 = 'https://yeezysupply.com/products/womens-suede-tubular-thigh-high-boots-110-mm-umber/?back=%2Fcollections%2Fseason-5-footwear'


class checkout():

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3000)
        self.base_url = url
        self.verificationErrors = []

    def run(self):
        driver = self.driver

        driver.get(self.base_url + "/")
        select = Select(driver.find_element_by_xpath(
            '//select'))
        # select by visible text
        select.select_by_visible_text(z)
        driver.find_element_by_xpath(
            '//*[@value="PURCHASE"]').click()

        driver.find_element_by_id("checkout_email").clear()
        driver.find_element_by_id("checkout_email").send_keys(email)

        driver.find_element_by_id(
            'checkout_shipping_address_first_name').clear()
        driver.find_element_by_id(
            'checkout_shipping_address_first_name').send_keys(firstname)

        driver.find_element_by_id(
            'checkout_shipping_address_last_name').clear()
        driver.find_element_by_id(
            'checkout_shipping_address_last_name').send_keys(lastname)

        driver.find_element_by_id('checkout_shipping_address_address1').clear()
        driver.find_element_by_id(
            'checkout_shipping_address_address1').send_keys(address1)

        driver.find_element_by_id('checkout_shipping_address_address2').clear()
        driver.find_element_by_id(
            'checkout_shipping_address_address2').send_keys(aPT)

        driver.find_element_by_id('checkout_shipping_address_city').clear()
        driver.find_element_by_id(
            'checkout_shipping_address_city').send_keys(cITY)

        select = Select(driver.find_element_by_id(
            'checkout_shipping_address_country'))
        # select by visible text
        select.select_by_visible_text(country)

        select = Select(driver.find_element_by_id(
            'checkout_shipping_address_province'))
        # select by visible text
        select.select_by_visible_text(state)

        driver.find_element_by_id('checkout_shipping_address_zip').clear()
        driver.find_element_by_id(
            'checkout_shipping_address_zip').send_keys(zIP)

        driver.find_element_by_id('checkout_shipping_address_phone').clear()
        driver.find_element_by_id(
            'checkout_shipping_address_phone').send_keys(phone)

        driver.find_element_by_xpath('//span[@class="btn__content"]').click()
        driver.find_element_by_xpath('//span[@class="btn__content"]').click()

        time.sleep(1)
        driver.switch_to.frame(0)

        

        driver.find_element_by_id('number').clear()
        driver.find_element_by_id("number").send_keys(credit_card_number)

       
        driver.switch_to_default_content()
        driver.switch_to.frame(1)

        xp1 = '(//*[@autocomplete="cc-name"])'
        driver.find_element_by_xpath(xp1).clear()
        driver.find_element_by_xpath(xp1).send_keys(firstname + ' ' + lastname)

        
        driver.switch_to_default_content()
        driver.switch_to.frame(2)

        driver.find_element_by_id("expiry").clear()
        driver.find_element_by_id("expiry").send_keys(credit_card_expiration_month + credit_card_expiration_year)

        
        driver.switch_to_default_content()
        driver.switch_to.frame(3)
        driver.find_element_by_id("verification_value").clear()
        driver.find_element_by_id("verification_value").send_keys(credit_card_crn)


        driver.switch_to_default_content()
        driver.find_element_by_id(
            "checkout_different_billing_address_false").click()
        driver.find_element_by_css_selector(
            "button[name=\"button\"] > span.btn__content").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True



def checker():
    x1 = process()
    found = False
    while(found == False):
        x2 = process()
        if(x1 != x2):
            # print the time
            print('found change')
            found = True
            order()
            
        else:
            localtime = time.localtime(time.time())
            print('Checked')
            time.sleep(1)
            
            links = x2
            


def process():
    links = []
    
    url = 'http://yeezysupply.com'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    for tag in soup.findAll('a', href=True):
        tag['href'] = urljoin(url, tag['href'])
        links.append(tag['href'])
    return(links)


def order():
    check = checkout()
    check.setUp()
    check.run()

print('Welcome to Yeezy Bot let the yeezus be with thee')
print('Please ensure this is all filled out correctly and everything is CaSe SenSitive especially country and state')
encryptions = ['33FD41CF38BCA','4494AEC78FE52','DB23B41D5B58B','supremememe','dotdotdash','oeoeoehs']
n = 12
while n > 1:
    key = input('License Key? ')
    if key in encryptions:
        encryptions.remove(key)
        n = 0
    else:
        print('Invalid try again or contact enan332@gmail.com')

firstname= input( 'First name')
lastname= input( 'Last name')
credit_card_number= input( 'Credit card #:')
credit_card_expiration_month= input( 'Expiration month | ex. 06|:')
credit_card_expiration_year= input( 'Expiration year |ex. 18 |:')
credit_card_crn= input( 'cvc security code: ')
address1 = input ('Street: ')
aPT= input('Apt,Suite: ')
cITY= input('City:')
state= input('State |ex. Illinois| :')
zIP = input('Zip: ')
country= input( 'Country |ex. United States| :')
phone= input( 'Phone:')
email= input( 'Email: ')
z = input('Size: ')
check = checkout()
    check.setUp()
checker()