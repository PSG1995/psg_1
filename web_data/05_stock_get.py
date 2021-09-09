from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

#코스피 정보 가져오기
kospi_info=soup.find("em", id="now_value")
print(kospi_info.text)

#거래량 천주 정보 가져오기
deal_info = soup.find('td', id='quant')
print("거래량", deal_info.text)

#거래량 장중 최고
max_price = soup.find("td", id="high_value")
print("장중최고", deal_info.text)

#거래량 52주 최고
tmp_index = soup.find("table", class_="table_kos_index")
tmp_52week = tmp_index.find_all("tr")[2].find("td")
print("52주 최고", tmp_52week.text)

# 시향뉴스 - ul
tmp_news = soup.find("ul", class_="sise_report")
# print(len(tmp_news))
# print(tmp_news)
tmp_li_all = tmp_news.find_all("span", class_="tit")
news = []
# str1 = ""
for one in tmp_li_all:
    news.append(one.text)
    # str1 = str1 + one.text + ","
# print(str1)
# 코스피 정보, 거래량(천주), 장중최고, 52주 최고, 시황뉴스

# no, 코스피정보, 거래량(천주), 장중최소, 52주 최고, 시황뉴스
#  1, ___,       ___,        ___,    ___,      ___
# 시황뉴스 목록을 csv파일로 만들기
import pandas as pd
dat = pd.DataFrame( { "시황뉴스":news } )
print(dat)
dat.to_csv("news.csv", index=False)
dat.to_excel("news_excel.xlsx", index=False)

# 이거 다시
# tmp_report = soup.find_all("ul", class_="sise_report")
# tmp_report2 = tmp_report.find_all("span", class_="tit")
# print(tmp_report2.text)
