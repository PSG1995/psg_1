# 코스닥 정보에 대한
# 지수 정보 20210908_14_index.csv
# 시황정보 뉴스 20210908_14_news.csv
# 시황정보 리포트 20210908_14_news.csv
# 인기검색어 20210908_14_pop_word.csv
# 가장 많이 본 뉴스 20210908_14_cnt_news.csv

from bs4 import BeautifulSoup
from urllib.request import urlopen

k_index_list = ["코스닥 지수", "거래량"]
k_index = []
url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSDAQ"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
# 코스닥 지수 element copy : <em id="now_value">1,039.69</em>

kosdaqinfo = soup.find("em", id="now_value")
k_index.append(kosdaqinfo.text)

deal_info = soup.find('td', id='quant')
print("거래량", deal_info.text)
k_index.append(deal_info.text)

import pandas as pd
dict_dat = { "구분":k_index_list, "지수":k_index }
all_dat = pd.DataFrame(dict_dat)
print(all_dat)
all_dat.to_csv("kosdaqinfo.csv", index=True)
all_dat.to_excel("kosdaqinfo.xlsx", index=True)

