from urllib.request import urlopen
from bs4 import BeautifulSoup

# url https://finance.naver.com/world/
# tag, id, class
# 다우산업지수, 나스닥 종합, S&P 500
# 다우산업지수 : dd, class:point_status

url = "https://finance.naver.com/sise/"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
print(soup.title)

data = soup.find("ul", class_="lst_pop")
dat_all=data.find_all("a")
value_all = data.find_all("span", class_="dn")
for one in dat_all:
    print(one.text)
for one in value_all:
    print(one.text)