from ast import Pass
import click
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time
import openpyxl as excel
import urllib.parse
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
from sys import platform

def readContacts(fileName):
    delay = 10
    f = open("message.txt",  encoding='utf-8')
    ads = f.read()
    f.close()
    ads = quote(ads)
    lst = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    firstCol = sheet['A']
    secondCol = sheet['B']
    driver = webdriver.Chrome(ChromeDriverManager().install())
    for cell in range(len(firstCol)):
        contact = str(firstCol[cell].value)
        message = str(secondCol[cell].value)
        link = "https://web.whatsapp.com/send?phone="+ contact +"&text="+ message + '%0A' + ads
        driver.get(link)
        print("Sending message to", contact)
        try:
            click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME , '_4sWnG')))
            click_btn.click() 
            sleep(5)
            print("Message sent successfuly")
        except :
            Pass
            print("Failed to send message")
    driver.quit()
targets = readContacts("./contact.xlsx")

