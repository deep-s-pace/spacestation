# 모듈 읽어오기
from ast import keyword
from re import S
from urllib import request
from bs4 import BeautifulSoup

# urlopen() 함수로 웹페이지 읽어오기
target = request.urlopen("https://www.google.com/finance/quote/.INX:INDEXSP?comparison=INDEXNASDAQ%3A.IXIC")
res = target.read()

#BeautifulSoup을 사용해 웹페이지 분석하기
soup = BeautifulSoup(res, 'html.parser') #beautifulsoup 객체생성
keywords = soup.find_all('div',class_='qIEjSe') #데이터에서 태그와 클래스를 찾는 함수
#get_text() == 데이터에서 문자열만 추출
#strip() == 데이터 양옆 공백 제거
keywords = [each_line.get_text().strip() for each_line in keywords]
print(keywords)

indexs = soup.find_all('span',class_='Z63m9d') #데이터에서 태그와 클래스를 찾는 함수
#get_text() == 데이터에서 문자열만 추출
#strip() == 데이터 양옆 공백 제거
indexs = [each_line.get_text().strip() for each_line in indexs]
print(indexs)