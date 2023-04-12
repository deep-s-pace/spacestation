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

today = date.today() # 오늘 날짜(초까지 나옴)
todayii = today.strftime("%y-%m-%d") # 형식 바꿔주기
todayi = today.strftime("%y%m%d")

# S&P Real Asset Index (USD)
# keyword9

driver = webdriver.Chrome('C:/Users/sdg/Desktop/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10) # seconds
url='https://www.spglobal.com/spdji/en/indices/multi-asset/sp-real-assets-index/#overview'
driver.get(url)
time.sleep(3)

# S&P Real Asset Index (USD) 지수추출
keyword9 = driver.find_element_by_class_name("published-value")
keyword9 = keyword9.text
print(keyword9)

# S&P Global Infrastructure TR(USD)
# keyword10

driver = webdriver.Chrome('C:/Users/sdg/Desktop/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10) # seconds

url2='https://www.spglobal.com/spdji/en/indices/equity/sp-global-infrastructure-index/#overview'
driver.get(url2)
time.sleep(3)

keyword10 = driver.find_element_by_class_name("published-value")
keyword10 = keyword10.text
print(keyword10)

conn=pymysql.connect(host='localhost', user='root', password='dldosdpvm1', db='indexs') 
curs = conn.cursor() 
sql = "INSERT INTO index_selenium (date,s_p_real_asset, s_p_global, krx_gb, hfri_rv, hfri_credit, cd, kospi, barclay_global) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);" 
curs.execute(sql,(todayii, keyword9, keyword10, keyword6, keyword12, keyword13, keyword15, keyword16, keyword17))

conn.commit()# 데이터 패치
conn.close()