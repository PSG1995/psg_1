from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
# print(soup.title)

## 코스피 정보 가져오기
kospi_info = soup.find("em", id = "now_value")
print('코스피정보', kospi_info.text)

## 거래량 천주 정보 가져오기
kospi_chunju = soup.find("td", id = "quant")
print('거래량(천주)', kospi_chunju.text)

## 거래량 장중 최고 가져오기
kospi_max = soup.find("td", id="high_value")
print('장중최고', kospi_max.text)

## 거래량 장중 최저 가져오기
kospi_min = soup.find("td", id="low_value")
print('장중최저', kospi_min.text)

## 거래량 52주 최고 가져오기
kospi_max52 = soup.find("table", class_="table_kos_index")
kospi_max52week = kospi_max52.find_all("tr")[2].find("td")
print('52주최고', kospi_max52week.text)

## 거래량 52주 최저 가져오기
kospi_min52 = soup.find("table", class_="table_kos_index")
kospi_min52week = kospi_min52.find_all("tr")[2].find_all("td")[1]
print('52주최저', kospi_min52week.text)

## 시황뉴스
kospi_news = soup.find("ul", class_="sise_report")
kospi_news2 = kospi_news.find("span", class_="tit")
print("시황뉴스", kospi_news2.text)

## 시황정보 리포트
## 모르겠음