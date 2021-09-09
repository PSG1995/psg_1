from bs4 import BeautifulSoup
from urllib.request import urlopen

k_news_list = ["코스닥 지수"]
k_news = []
url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSDAQ"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')

kosdaqnews = soup.find("ul", class_="sise_report")
k_news.append(kosdaqnews.text)

import pandas as pd
kosdaq_dict_dat = { "구분":k_news_list, "지수":k_news }
kosdaq_all_dat = pd.DataFrame(kosdaq_dict_dat)
print(kosdaq_all_dat)
kosdaq_all_dat.to_csv("kosdaqnews.csv", index=True)
kosdaq_all_dat.to_excel("kosdaqnews.xlsx", index=True)