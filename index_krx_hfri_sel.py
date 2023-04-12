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

# KRX GB Index
# keyword6

driver = webdriver.Chrome('C:/Users/sdg/Desktop/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10) # seconds

url6='http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201010101'
driver.get(url6)
time.sleep(3)

keyword6 = driver.find_element_by_class_name("CI-GRID-ALIGN-RIGHT")
keyword6 = keyword6.text
print(keyword6)

#HFRI RV: Fixed Income-Convertible Arbitrage Index(USD)
#keyword12

driver = webdriver.Chrome('C:/Users/sdg/Desktop/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10) # seconds

url12='https://www.hfr.com/indices/hfri-rv-fixed-income-convertible-arbitrage-index'
driver.get(url12)
time.sleep(3)

driver.find_element_by_xpath('/html/body/section/section[3]/div/div/div[2]/div/div[1]/div/section[1]/form/div/div[1]/input').send_keys("miniunisim@gmail.com")
driver.find_element_by_xpath('/html/body/section/section[3]/div/div/div[2]/div/div[1]/div/section[1]/form/div/div[2]/input').send_keys("awse20121014")
driver.implicitly_wait(5)
driver.find_element_by_xpath('/html/body/section/section[3]/div/div/div[2]/div/div[1]/div/section[1]/form/div/div[3]/button').click()
driver.implicitly_wait(15)

keyword12s = driver.find_element_by_class_name("amChartsLegend.amcharts-legend-div").text
keyword12 = keyword12s[-9:]
print(keyword12)