from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import*
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import os
from dotenv import load_dotenv
load_dotenv()

browser = webdriver.Chrome('XXX')

browser.get("https://wish.wis.ntu.edu.sg/pls/webexe/ldap_login.login?w_url=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_planner.main")
element = browser.find_element_by_xpath('//*[@id="UID"]')
element.send_keys(os.getenv('USERNAME'))
element = (browser.find_element_by_xpath('//*[@id="DOMAIN"]/option[1]')).click()
element = browser.find_element_by_xpath('//*[@id="top"]/div/section[2]/div/div/center[1]/form/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input[1]')
element.send_keys(Keys.RETURN)

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PW"]')))

element = browser.find_element_by_xpath('//*[@id="PW"]')
element.send_keys(os.getenv('PASSWORD'))
element = browser.find_element_by_xpath('//*[@id="top"]/div/section[2]/div/div/form/center[1]/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]')
element.send_keys(Keys.RETURN)

while True:
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/form[2]/div/div[3]/div/div/section[2]/div/div/p/table/tbody/tr[1]/td[2]/table/tbody/tr[11]/td/form/input[1]')))
    browser.find_element_by_xpath('/html/body/form[2]/div/div[3]/div/div/section[2]/div/div/p/table/tbody/tr[1]/td[2]/table/tbody/tr[11]/td/form/input[1]').click()
    try: 
        alert = browser.switch_to.alert
        if alert.text.find('not allowed to register'):
            alert.accept()
            continue
        else: 
            alert.accept()
            break
    except:
        break