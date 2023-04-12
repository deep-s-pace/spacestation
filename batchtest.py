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

# 날짜 반복문 테스트

from datetime import datetime, timedelta 

# 시작일,종료일 설정 
start = "2016-08-01" 
last = "2021-08-04" 

# 시작일, 종료일 datetime 으로 변환 
start_date = datetime.strptime(start, "%Y-%m-%d") 
last_date = datetime.strptime(last, "%Y-%m-%d") 

# 종료일 까지 반복 
while start_date <= last_date: 
    dates = start_date.strftime("%Y-%m-%d") 
    print(dates) 
    
    # 하루 더하기 
    start_date += timedelta(days=1)