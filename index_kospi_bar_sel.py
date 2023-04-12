from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from ast import keyword
from re import S
from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import pymysql
import schedule
import time
from datetime import date

# HFRI Credit Index(USD)
# keyword13

url13='https://www.hfr.com/indices/hfri-credit-index'
driver.get(url13)
time.sleep(3)

keyword13s = driver.find_element_by_class_name("amcharts-main-div").text
keyword13 = keyword13s[24:32]
print(keyword13)

# Kospi
# keyword16

driver = webdriver.Chrome('C:/Users/sdg/Desktop/chromedriver_win32/chromedriver.exe')
krx_url='http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201010101'
driver.get(krx_url)
driver.implicitly_wait(3)

driver.find_element_by_xpath('/html/body/div[2]/section[2]/section/section/div/div/form/div[1]/div/table/tbody/tr[1]/td/label[2]').click()
driver.find_element_by_xpath('/html/body/div[2]/section[2]/section/section/div/div/form/div[1]/div/a').click()

keyword16 = driver.find_element_by_class_name("CI-GRID-ALIGN-RIGHT").text
print(keyword16)

#soup = BeautifulSoup(html, 'html.parser')
#kospi = soup.find_all('td', class_='CI-GRID-ALIGN-RIGHT')
#kospi = [each_line.get_text().strip() for each_line in kospi]
#kospi = kospi[9]
#print(kospi)

#Barclays Global Index(USD)
# keyword17

driver = webdriver.Chrome('C:/Users/sdg/Desktop/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10) # seconds

url17='https://indices.barclays/IM/33/en/indices/details.app;ticker=BXIISG6E'
driver.get(url17)
time.sleep(3)

driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/button[2]').click()
driver.implicitly_wait(15)
driver.find_element_by_xpath('/html/body/idx-root/voyager-app-root/div/voyager-app-modal/voyager-modal/div/div[1]/div[2]/div/button[1]').click()
driver.implicitly_wait(15)

keyword17 = driver.find_element_by_class_name("level")
keyword17 = keyword17.text
print(keyword17)