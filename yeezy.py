# imports, imports galore, yay
import json
import time
import httplib2
import lxml
import requests
from random import randint
from BeautifulSoup import BeautifulSoup, SoupStrainer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

#not really sure what this does or why but it's necesary
driver = webdriver.Firefox()
orderinf = []
try:
        confFile = open("order.conf")
        orderinf = json.loads(confFile.read())["orders"]
except Exception as e:
                print('Error: either no checkout.conf was found, Error Details: ' + str(e))

def order():
    i = 0
    url = []
    
    # select the url in href for all a tags(links)
    #god why is http so dang hard and why cant it just work
    http = httplib2.Http()
    status, response = http.request('http://www.yeezysupply.com')
    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        if link.has_attr('href'):
            url[i] = link['href']
            print(url[i])
    for x in url-11:
            y = randint(30,45)
            payload = {'size':y}
            requests.post(url[x],payload)


order()
# CHECK MAY NOT NEED FUNCTION

# exec
def checkout():
        #to the devs of the yeezy checkout wtf is wrong with that your naming conventions 
        # are worse then a flippen high school robotics team
    payload = {
        "First name": "Elijah",
        "Last name": "Boostman",
        "APT/SUITE": "Unit A",
        "CITY": "Redondo Beach",
        "State": "California",
        "ZIP CODE": "90277",
        "Country":"XXXXXX",
        "Phone": "55555555",
        "Email": "XXXXXXXXX"}
#FIND THE DANG CHECKOUT LINK
    r = requests.post("", data=payload)
    print(r.text)

#finish the bloody checkout code
    payload = {
        "First name": "Elijah",
        "Last name": "Boostman",
        "credit_card_number": "555555555555",
        "credit_card_expiration_month": "5",
        "credit_card_expiration_year": "2018",
        "credit_card_crn": "234",
        }
    print('Shoe Copped; Check Email')
