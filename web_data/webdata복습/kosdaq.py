from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSDAQ"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
k_index_list = ['코스닥지수', '거래량']
k_index = []

kosdaq_info = soup.find('em', id = 'now_value')
# print(kosdaq_info)
k_index.append(kosdaq_info.text)

deal_info = soup.find('td', id="quant")
k_index.append(deal_info.text)

import pandas as pd
dict_dat = {"구분": k_index_list, "지수": k_index}
all_dat = pd.DataFrame(dict_dat)
print(all_dat)
all_dat.to_csv("kosdaq_info.csv", index=True)
all_dat.to_excel("kosdaq_info.xlsx", index=True)
