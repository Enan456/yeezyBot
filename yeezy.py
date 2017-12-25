#imports
import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

email = 'test'
firstname = 'test'
lastname = 'test'
driver = webdriver.Firefox()

def order():

    connection = urllib.urlopen('http://www.yeezysupply.com')

    dom = lxml.html.fromstring(connection.read())
    i = 0
    # select the url in href for all a tags(links)
    for link in dom.xpath('//a/@href'):
        url[i] = link


def checkout():
    print('********************************')
    print('********************************')
    print('********************************')
    print('***********CartCopper***********')
    print('**************FOR***************')
    print('********************************')
    print('*************yeezy**************')
    print('********************************')
    print('********************************')
    print('********************************')
    statenum = 1
    ccmonthn = 1
    ccyear = 1
    confFile = None
    orders = []
    for order in orders:
# state
        states = order['state']
        if states == ('AA Military'):
            statenum = 2
        if states == ('AE Military'):
            statenum = 3
        if states == ('AP Military'):
            statenum = 4
        if states == ('Alabama'):
            statenum = 5
        if states == ('Alaska'):
            statenum = 6
        if states == ('Arizona'):
            statenum = 7
        if states == ('Arkansas'):
            statenum = 8
        if states == ('California'):
            statenum = 9
        if states == ('Colorado'):
            statenum = 10
        if states == ('Connecticut'):
            statenum = 11
        if states == ('Delaware'):
            statenum = 12
        if states == ('District of Colombia'):
            statenum = 13
        if states == ('Florida'):
            statenum = 14
        if states == ('Georgia'):
            statenum = 15
        if states == ('Hawaii'):
            statenum = 16
        if states == ('Idaho'):
            statenum = 17
        if states == ('Illinois'):
            statenum = 18
        if states == ('Indiana'):
            statenum = 19
        if states == ('Iowa'):
            statenum = 20
        if states == ('Kansas'):
            statenum = 21
        if states == ('Kentucky'):
            statenum = 22
        if states == ('Louisiana'):
            statenum = 23
        if states == ('Maine'):
            statenum = 24
        if states == ('Maryland'):
            statenum = 25
        if states == ('Massachusetts'):
            statenum = 26
        if states == ('Michigan'):
            statenum = 27
        if states == ('Minnesota'):
            statenum = 28
        if states == ('Mississippi'):
            statenum = 29
        if states == ('Missouri'):
            statenum = 30
        if states == ('Montana'):
            statenum = 31
        if states == ('Nebraska'):
            statenum = 32
        if states == ('Nevada'):
            statenum = 33
        if states == ('New Hampshire'):
            statenum = 34
        if states == ('New Jersey'):
            statenum = 35
        if states == ('New Mexico'):
            statenum = 36
        if states == ('New York'):
            statenum = 37
        if states == ('North Carolina'):
            statenum = 38
        if states == ('North Dakota'):
            statenum = 39
        if states == ('Ohio'):
            statenum = 40
        if states == ('Oklahoma'):
            statenum = 41
        if states == ('Oregon'):
            statenum = 42
        if states == ('Pennsylvania'):
            statenum = 43
        if states == ('Rhode Island'):
            statenum = 44
        if states == ('South Carolina'):
            statenum = 45
        if states == ('South Dakota'):
            statenum = 46
        if states == ('Tennessee'):
            statenum = 47
        if states == ('Texas'):
            statenum = 48
        if states == ('Utah'):
            statenum = 49
        if states == ('Vermont'):
            statenum = 50
        if states == ('Virginia'):
            statenum = 51
        if states == ('Washington'):
            statenum = 52
        if states == ('West Virginia'):
            statenum = 53
        if states == ('Wisonsin'):
            statenum = 54
        if states == ('Wyoming'):
            statenum = 55

 # cc month
        ccmonths = order['credit_card_expiration_month']
        if ccmonths == ('1'):
            ccmonth = 2
        if ccmonths == ('2'):
            ccmonth = 3
        if ccmonths == ('3'):
            ccmonth = 4
        if ccmonths == ('4'):
            ccmonth = 5
        if ccmonths == ('5'):
            ccmonth = 6
        if ccmonths == ('6'):
            ccmonth = 7
        if ccmonths == ('7'):
            ccmonth = 8
        if ccmonths == ('8'):
            ccmonth = 9
        if ccmonths == ('9'):
            ccmonth = 10
        if ccmonths == ('10'):
            ccmonth = 11
        if ccmonths == ('11'):
            ccmonth = 12
        if ccmonths == ('12'):
            ccmonth = 13

# cc year
        ccyears = order['credit_card_expiration_year']
        if ccyears == ('2017'):
            ccyear = 2
        if ccyears == ('2018'):
            ccyear = 3
        if ccyears == ('2019'):
            ccyear = 4
        if ccyears == ('2020'):
            ccyear = 5
        if ccyears == ('2021'):
            ccyear = 6
        if ccyears == ('2022'):
            ccyear = 7
        if ccyears == ('2023'):
            ccyear = 8
        if ccyears == ('2024'):
            ccyear = 9
        if ccyears == ('2025'):
            ccyear = 10
        if ccyears == ('2026'):
            ccyear = 11
        if ccyears == ('2027'):
            ccyear = 12
        if ccyears == ('2028'):
            ccyear = 13
        if ccyears == ('2029'):
            ccyear = 14
        if ccyears == ('2030'):
            ccyear = 15
        if ccyears == ('2031'):
            ccyear = 16
        if ccyears == ('2032'):
            ccyear = 17
        if ccyears == ('2033'):
            ccyear = 18
        if ccyears == ('2034'):
            ccyear = 19
        if ccyears == ('2035'):
            ccyear = 20
        if ccyears == ('2036'):
            ccyear = 21
        if ccyears == ('2037'):
            ccyear = 22

# exec
        checker = driver.find_element_by_css_selector(
            '.myaccount-your-items-product a').get_attribute('href')
        print(checker)
        CheckerTest = input("Does URL Look Like The Shoe You Want? Y or N:")
        if CheckerTest == 'N' or CheckerTest == 'n':
            print('Faulty Cart, Do Not But')
        if CheckerTest == 'Y' or CheckerTest == 'y':
            payload = {
                "first": "Elijah",
                "last": "Boostman",
                "address": "Addy 101",
                "unit": "Unit A",
                "city": "Redondo Beach",
                "state": "California",
                "zip": "90277",
                "phone": "9110294444",
                "credit_card_number": "4147222100932835",
                "credit_card_expiration_month": "8",
                "credit_card_expiration_year": "2018",
                "credit_card_crn": "234"}
            r = requests.post("http://httpbin.org/post", data=payload)
            print(r.text)
            print('Shoe Copped; Check Email')
