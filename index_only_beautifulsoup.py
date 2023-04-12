from ast import keyword
from re import S
from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import pymysql
import schedule
import time

 #Dow Jones Global Equity Yield Index

target = request.urlopen("https://www.google.com/finance/quote/DJGEQY:INDEXDJX")
res = target.read()

    #BeautifulSoup을 사용해 웹페이지 분석하기
soup = BeautifulSoup(res, 'html.parser') #beautifulsoup 객체생성
keywords = soup.find_all('div',class_='P6K39c') #데이터에서 태그와 클래스를 찾는 함수
    #get_text() == 데이터에서 문자열만 추출
    #strip() == 데이터 양옆 공백 제거
keywords = [each_line.get_text().strip() for each_line in keywords]
keyword = keywords[0]
    #keyword = keyword.replace(',','')
print(keyword)

time.sleep(10)

    # Dow Jones Brookfield Global Infrastructure(USD)

target2 = request.urlopen("https://www.google.com/finance/quote/DJBGIE:INDEXDJX")
res2 = target2.read()

    #BeautifulSoup을 사용해 웹페이지 분석하기
soup = BeautifulSoup(res2, 'html.parser') #beautifulsoup 객체생성
keyword2s = soup.find_all('div',class_='P6K39c') #데이터에서 태그와 클래스를 찾는 함수
    #get_text() == 데이터에서 문자열만 추출
    #strip() == 데이터 양옆 공백 제거
keyword2s = [each_line.get_text().strip() for each_line in keyword2s]
keyword2 = keyword2s[0]
    #keyword2 = keyword2.replace(',','')
print(keyword2)

time.sleep(10)

    # Dow Jones Global ex-US Select Real Estate Securities

target3 = request.urlopen("https://www.google.com/finance/quote/DWXRS:INDEXDJX?sa=X&ved=2ahUKEwigsLCM94X2AhUPc5QKHS1vBWEQ3ecFegQIGxAc")
res3 = target3.read()

    #BeautifulSoup을 사용해 웹페이지 분석하기
soup = BeautifulSoup(res3, 'html.parser') #beautifulsoup 객체생성
keyword3s = soup.find_all('div',class_='P6K39c') #데이터에서 태그와 클래스를 찾는 함수
#get_text() == 데이터에서 문자열만 추출
    #strip() == 데이터 양옆 공백 제거
keyword3s = [each_line.get_text().strip() for each_line in keyword3s]
keyword3 = keyword3s[0]
    #keyword3 = keyword3.replace(',','')
print(keyword3)

time.sleep(10)

    # S&P Listed Private Equity Index(USD)

target4 = request.urlopen("https://www.google.com/finance/quote/SPLPEQTY:INDEXSP")
res4 = target4.read()

    #BeautifulSoup을 사용해 웹페이지 분석하기
soup = BeautifulSoup(res4, 'html.parser') #beautifulsoup 객체생성
keyword4s = soup.find_all('div',class_='P6K39c') #데이터에서 태그와 클래스를 찾는 함수
    #get_text() == 데이터에서 문자열만 추출
    #strip() == 데이터 양옆 공백 제거
keyword4s = [each_line.get_text().strip() for each_line in keyword4s]
keyword4 = keyword4s[0]
    #keyword4 = keyword4.replace(',','')
print(keyword4)

time.sleep(10)

    # S&P 500 Real Estate Index(USD)

target5 = request.urlopen("https://www.google.com/finance/quote/SP500-60:INDEXSP")
res5 = target5.read()

    #BeautifulSoup을 사용해 웹페이지 분석하기
soup = BeautifulSoup(res5, 'html.parser') #beautifulsoup 객체생성
keyword5s = soup.find_all('div',class_='P6K39c') #데이터에서 태그와 클래스를 찾는 함수
    #get_text() == 데이터에서 문자열만 추출
    #strip() == 데이터 양옆 공백 제거
keyword5s = [each_line.get_text().strip() for each_line in keyword5s]
keyword5 = keyword5s[0]
    #keyword5 = keyword5.replace(',','')
print(keyword5)

time.sleep(10)

    # LPX50 Listed Private Equity Index TR (USD)

target7 = request.urlopen("https://www.lpx-group.com/chart/?index=CH0022737545")
res7 = target7.read()

    #BeautifulSoup을 사용해 웹페이지 분석하기
soup = BeautifulSoup(res7, 'html.parser') #beautifulsoup 객체생성
keyword7s = soup.find_all('td', class_='charttable') #데이터에서 태그와 클래스를 찾는 함수
    #get_text() == 데이터에서 문자열만 추출
    #strip() == 데이터 양옆 공백 제거
keyword7s = [each_line.get_text().strip() for each_line in keyword7s]
keyword7 = keyword7s[4]
keyword7 = keyword7[0:7] #값 뒤에 ()제거
    #keyword6 = keyword6.replace(',','')
print(keyword7)

time.sleep(10)

    # DLX Direct Lending Index TR

target8 = request.urlopen("https://www.lpx-group.com/chart/?index=CH0036304076")
res8 = target8.read()

    #BeautifulSoup을 사용해 웹페이지 분석하기
soup = BeautifulSoup(res8, 'html.parser') #beautifulsoup 객체생성
keyword8s = soup.find_all('td', class_='charttable') #데이터에서 태그와 클래스를 찾는 함수
    #get_text() == 데이터에서 문자열만 추출
    #strip() == 데이터 양옆 공백 제거
keyword8s = [each_line.get_text().strip() for each_line in keyword8s]
keyword8 = keyword8s[4]
keyword8 = keyword8[0:7] #값 뒤에 ()제거
    #keyword6 = keyword6.replace(',','')
print(keyword8)

time.sleep(10)

    # 원달러환율

    # 403:Forbidden 에러 발생하여 새롭게 urlopen해야됨
from urllib.request import Request, urlopen
req = Request('https://kr.investing.com/currencies/usd-krw', headers={'User-Agent': 'Mozilla/5.0'})
    #target11 = request.urlopen("https://kr.investing.com/currencies/usd-krw")
res11 = urlopen(req).read()

    #BeautifulSoup을 사용해 웹페이지 분석하기
soup = BeautifulSoup(res11, 'html.parser') #beautifulsoup 객체생성
keyword11s = soup.find_all('div', class_='trading-hours_value__2MrOn') #데이터에서 태그와 클래스를 찾는 함수
    #get_text() == 데이터에서 문자열만 추출
    #strip() == 데이터 양옆 공백 제거
keyword11s = [each_line.get_text().strip() for each_line in keyword11s]
keyword11 = keyword11s[0]
    #keyword6 = keyword6.replace(',','')
print(keyword11)

time.sleep(10)

from datetime import date
today = date.today() # 오늘 날짜(초까지 나옴)
today = today.strftime("%y-%m-%d") # 형식 바꿔주기

conn=pymysql.connect(host='localhost', user='root', password='dldosdpvm1', db='indexs')
curs = conn.cursor()
sql = "INSERT INTO index_beautiful (date,d_j_equity,d_j_brook,d_j_ex_us,s_p_list,s_p500,lpx50,dlx_direct,exchange) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
curs.execute(sql,(today, keyword, keyword2, keyword3, keyword4, keyword5, keyword7, keyword8, keyword11))

conn.commit()# 데이터 패치
conn.close()