import os
from pickle import TRUE
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
    print(i)
    
#Refresh Browser new cookie
driver.refresh()

#tunggu reload dulu 
time.sleep(10)

#Wait javascript loaded
driver.execute_script("return document.readyState")

#Open page Hack Input profile ban
listIframe = [
    'tab=people_and_other_pages&cquick=jsc_c_u&cquick_token=AQ5CqNyaWgIrd2D2ASo&ctarget=https%3A%2F%2Fweb.facebook.com',
    'tab=people_and_other_pages&cquick=jsc_c_14&cquick_token=AQ5CqNyaWgIrd2D2BpI&ctarget=https%3A%2F%2Fweb.facebook.com',
    'tab=people_and_other_pages&cquick=jsc_c_11&cquick_token=AQ5CqNyaWgIrd2D22Gg&ctarget=https%3A%2F%2Fweb.facebook.com'
]
#MEMBUKA LINK IFRAME FORM BLOK PROFILE
driver.get(listIframe[0])
#TUNGGU 3 DETIK
time.sleep(3)
#MEMBUKA LINK HALAMAN YG LAIN
countI = 0
for i in listIframe:
    if countI != 0:
        driver.execute_script(f'''window.open("{i}","_blank");''')
        time.sleep(2)
    countI += 1
    
#BERPINDAH PINDAH TAB
tabs = driver.window_handles

for i in tabs:
    time.sleep(2)
    driver.switch_to.window(i)

def setUpFormBlokir():
    #klik option pilih orang dan halaman yang di larang
    try:
        WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.NAME, 'query_edge_selector'))
            ).click()
        try:
            WebDriverWait(driver, 50).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[text()='Orang dan Halaman yang Dilarang']"))
                ).click()
            
            #mengisi form pencarian dengan xxxxx
            cariorang = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Cari"]'))
                )
            cariorang.send_keys("xxxxxx")
        except TimeoutException:
            return False
        
        #Jeda 5 detik 
        time.sleep(5)
        
        #klik button larang seseorang
        try:
            WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Larang Seseorang"]'))
                ).click()
        except TimeoutException:
            return False
        
        
        return True
    except TimeoutException:
        return False
    
#pindah ke tab pertama [0] 
driver.switch_to.window(tabs[0])
if setUpFormBlokir() : 
    print(f'Oke prepare form Blokir tabs-{tabs[0]} redy')
else: 
    print(f'Gagal prepare form Blokir tabs-{tabs[0]}')
    driver.quit()
#pindah ke tab pertama [1] 
driver.switch_to.window(tabs[1])
time.sleep(2)
if setUpFormBlokir() : 
    print(f'Oke prepare form Blokir tabs-{tabs[1]} redy')
else: 
    print(f'Gagal prepare form Blokir tabs-{tabs[1]}')
    driver.quit()
#pindah ke tab pertama [2] 
driver.switch_to.window(tabs[2])
time.sleep(2)
if setUpFormBlokir() : 
    print(f'Oke prepare form Blokir tabs-{tabs[2]} redy')
else: 
    print(f'Gagal prepare form Blokir tabs-{tabs[2]}')
    driver.quit()

# Input link ke text/ search link to baned    
def inputProfileToBan(link):
    time.sleep(7)
    try:
        textInput = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-haspopup="listbox"]'))
            )
        textInput.clear()
        textInput.send_keys(link)
        time.sleep(3)
        WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul[role="listbox"] li[role="option"] div[class="clearfix"]'))
            ).click()
        print("Berhasil terinput")
        #klik button simpan blokir
        WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Simpan"]'))
            ).click()
        time.sleep(4)
        # klik button konfirmasi blokir 
        WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Konfirmasi"]'))
            ).click()
        time.sleep(3)
        # klik button tutup done
        WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Tutup'))
            ).click()
        
        return True
    except TimeoutException:
        return False

# eksekusi blokir data
   
dataListBan = open('data-ban.txt', 'r').read().splitlines()
dataListBan = [i for i in dataListBan if i]

#loop data blokir
for linkProfile in dataListBan:
    #loop tabs/ blokir perhalaman
   
    for tb in tabs:
        #jeda 
        time.sleep(3)
        #pindah tabs
        driver.switch_to.window(tb)
        #perintah blokir
        if inputProfileToBan(linkProfile):
            print('sukses input |'+ linkProfile)
        else:
            print("Gagal total | " + linkProfile)
    
    

    



        
