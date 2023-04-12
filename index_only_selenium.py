from ast import keyword
from re import S
from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import pymysql
import schedule
import time


time.sleep(600)
# S&P Real Asset Index (USD)
# keyword9

driver = webdriver.Chrome('C:/Users/sdg/Desktop/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10) # seconds
url='https://www.spglobal.com/spdji/en/indices/multi-asset/sp-real-assets-index/#overview'
driver.get(url)
time.sleep(10)

# S&P Real Asset Index (USD) 지수추출
keyword9 = driver.find_element_by_class_name("published-value")
keyword9 = keyword9.text
print(keyword9)

time.sleep(60)
# S&P Global Infrastructure TR(USD)
# keyword10

driver = webdriver.Chrome('C:/Users/sdg/Desktop/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10) # seconds

url2='https://www.spglobal.com/spdji/en/indices/equity/sp-global-infrastructure-index/#overview'
driver.get(url2)
time.sleep(5)

keyword10 = driver.find_element_by_class_name("published-value")
keyword10 = keyword10.text
print(keyword10)

time.sleep(60)
# KRX GB Index
# keyword6

driver = webdriver.Chrome('C:/Users/sdg/Desktop/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10) # seconds

url6='http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201010101'
driver.get(url6)
time.sleep(5)

keyword6 = driver.find_element_by_class_name("CI-GRID-ALIGN-RIGHT")
keyword6 = keyword6.text
print(keyword6)

time.sleep(60)
# HFRI RV: Fixed Income-Convertible Arbitrage Index(USD)
# keyword12

driver = webdriver.Chrome('C:/Users/sdg/Desktop/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10) # seconds

url12='https://www.hfr.com/indices/hfri-rv-fixed-income-convertible-arbitrage-index'
driver.get(url12)
time.sleep(3)

driver.find_element_by_xpath('/html/body/section/section[3]/div/div/div[2]/div/div[1]/div/section[1]/form/div/div[1]/input').send_keys("miniunisim@gmail.com")
driver.find_element_by_xpath('/html/body/section/section[3]/div/div/div[2]/div/div[1]/div/section[1]/form/div/div[2]/input').send_keys("awse20121014")
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/section/section[3]/div/div/div[2]/div/div[1]/div/section[1]/form/div/div[3]/button').click()
driver.implicitly_wait(25)

keyword12s = driver.find_element_by_class_name("amcharts-main-div").text
keyword12 = keyword12s
print(keyword12)


time.sleep(40)
# HFRI Credit Index(USD)
# keyword13

url13='https://www.hfr.com/indices/hfri-credit-index'
driver.get(url13)
time.sleep(10)

keyword13s = driver.find_element_by_class_name("amcharts-main-div").text
keyword13 = keyword13s[24:32]
print(keyword13)


time.sleep(120)
# Cd
# keyword15

driver = webdriver.Chrome('C:/Users/sdg/Desktop/chromedriver_win32/chromedriver.exe')
url='http://ecos.bok.or.kr/flex/EasySearch.jsp?langGubun=K&topCode=060Y001'
driver.get(url)
driver.implicitly_wait(15)
driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div/div/div[3]/div/section[2]/div[2]/div/div/div[2]/div/div/div[6]/div/div/div/div/table/tbody/tr[5]/td/div[1]/div[2]/div/span').click()
driver.implicitly_wait(25)
driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div/div/div[3]/div/section[3]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div[1]/input').send_keys(todayi)
driver.implicitly_wait(25)
driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div/div/div[3]/div/section[3]/div[1]/div[1]/div[2]/div/div/div/div').click()

html = driver.page_source
    #BeautifulSoup을 사용해 웹페이지 분석하기
soup = BeautifulSoup(html, 'html.parser') #beautifulsoup 객체생성
keyword15 = soup.find_all('td', class_= '') #데이터에서 태그와 클래스를 찾는 함수
    #get_text() == 데이터에서 문자열만 추출
    #strip() == 데이터 양옆 공백 제거
keyword15 = [each_line.get_text().strip() for each_line in keyword15]
keyword15 = keyword15[4]
print(keyword15)


time.sleep(120)
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


time.sleep(120)
# Barclays Global Index(USD)
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


time.sleep(30)
conn=pymysql.connect(host='localhost', user='root', password='dldosdpvm1', db='indexs') 
curs = conn.cursor() 
sql = "INSERT INTO index_selenium (date,s_p_real_asset, s_p_global, krx_gb, hfri_rv, hfri_credit, cd, kospi, barclay_global) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);" 
curs.execute(sql,(todayii, keyword9, keyword10, keyword6, keyword12, keyword13, keyword15, keyword16, keyword17))

conn.commit()# 데이터 패치
conn.close()