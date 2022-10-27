#imports here

import os
from select import select
from tkinter import ANCHOR
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from csv import DictReader
import time

#PATH CHROME  DRIVER
PathCD = 'C:/Users/ASUS/Documents/Doing/chromedriver_win32/chromedriver.exe'


#code by pythonjar, SETUP OPTION CHROME
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome(PathCD, chrome_options=chrome_options)
driver.maximize_window()

#open the webpage
driver.get("http://www.facebook.com")

#Add cookie login FB
def getCookieValues(filename):
    with open(filename, encoding='utf-8-sig') as f:
        dict_reader = DictReader(f)
        lis_of_dicts = list(dict_reader)
        
    return lis_of_dicts

Cookiesfb = getCookieValues('fb-cookie.csv')

for i in Cookiesfb:
    driver.add_cookie(i)
    
#Refresh Browser
driver.refresh()    

#Wait page / wait loaded
# time.sleep(10)

# #Open page ban FP
# urlBlock = 'https://web.facebook.com/bataminfinxharbolnaz/settings/?tab=people_and_other_pages'

# driver.get(urlBlock)

#Wait page / wait loaded
time.sleep(10)

#Wait javascript loaded
driver.execute_script("return document.readyState")

#Open page Hack Input profile ban
# inframe list
# 1. Batam infinix =  https://web.facebook.com/Batam-lnfinix-102312909313422/settings/?tab=people_and_other_pages&cquick=jsc_c_12&cquick_token=AQ4DWTCnol5kGWWD9Y0&ctarget=https%3A%2F%2Fweb.facebook.com
# 2. Batam Harbolnas = https://web.facebook.com/batamlnfinix/settings/?tab=people_and_other_pages&cquick=jsc_c_u&cquick_token=AQ6d-q2mQfhRlWA-7_Y&ctarget=https%3A%2F%2Fweb.facebook.com
# 3. bataminfinxharbolnaz = https://web.facebook.com/bataminfinxharbolnaz/settings/?tab=people_and_other_pages&cquick=jsc_c_12&cquick_token=AQ6d-q2mQfhRlWA-rk4&ctarget=https%3A%2F%2Fweb.facebook.com

inframeblock = 'https://web.facebook.com/Batam-lnfinix-102312909313422/settings/?tab=people_and_other_pages&cquick=jsc_c_12&cquick_token=AQ4DWTCnol5kGWWD9Y0&ctarget=https%3A%2F%2Fweb.facebook.com'

driver.get(inframeblock)

# pageSource = driver.page_source
# print(pageSource)

# fileToWrite = open("page_source.html", "w")
# fileToWrite.write(pageSource)
# fileToWrite.close()


#Proces add data baned fp
try:
    
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME, 'query_edge_selector'))).click()
    
    time.sleep(5)
        
    try:
        WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Orang dan Halaman yang Dilarang']"))).click()
        cariorang = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Cari"]')))
        cariorang.send_keys("xxxxxx")
        print("oke seep 1")
    except TimeoutException:
        print("gagal clik 1")    
                
    time.sleep(10)
    
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Larang Seseorang"]'))).click()
        print("oke seep 2")
    except TimeoutException:
        print("gagal clik larang")
    
    InputLink = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Ketikkan nama atau email teman"]')))
    try:   
        InputLink.clear()
        InputLink.send_keys("https://web.facebook.com/profile.php?id=100049544145919&_rdc=1&_rdr")
        time.sleep(10) 
        print("oke seep 3")
    except TimeoutException:
        InputLink.clear()
        InputLink.send_keys('')
        print("Gagal input link ban") 
        
    #Css Selector : ul[role="listbox"] li[role="option"] div[class="clearfix"]
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul[role="listbox"] li[role="option"] div[class="clearfix"]'))).click()
        print("ok seep 4")
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Simpan"]'))).click()
        time.sleep(7)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Konfirmasi"]'))).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Tutup'))).click()
        print('sukses input')
        
    except TimeoutException:
        print('gagal klik user ban')
        
        
    dataListBan = open('data-ban.txt', 'r').read().splitlines()
    dataListBan = [i for i in dataListBan if i]
    inputprofileBan = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Ketikkan nama atau email teman"]')))
    
    for linkProfile in dataListBan : 
        try: 
            inputprofileBan.clear()
            inputprofileBan.send_keys(linkProfile)
            time.sleep(3)
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul[role="listbox"] li[role="option"] div[class="clearfix"]'))).click()
            print("ok seep 4")
            time.sleep(3)
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Simpan"]'))).click()
            time.sleep(5)
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Konfirmasi"]'))).click()
            time.sleep(4)
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Tutup'))).click()
            print('sukses input |'+ linkProfile)
            
        except TimeoutException:
            print("Gagal total | " + linkProfile)
            inputprofileBan.send_keys('')
           
            
    print('sucses full')
    
except TimeoutException:
    
    print('proses input data Gagal')
    
    