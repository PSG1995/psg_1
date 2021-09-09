from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import time

url = 'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=37886&target=after'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')


##1~50페이지 가져오기

basic_url = 'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=37886&target=after&page='
comment_5 = []
for i in range(1,51,1):
    real_url = basic_url + str(i)
    page = urlopen(real_url)
    soup = BeautifulSoup(page, 'html.parser')
    comment_all = soup.find_all('td', class_='title')
    print(len(comment_all))

    # comments = []
    for one in comment_all:
        temp = list(one.children)[6].strip()
        # print(temp)
        comment_5.append(temp)

    time.sleep(1)
print(len(comment_5), comment_5)

dict_dat = {"댓글":comment_5}
dat = pd.DataFrame(dict_dat)
dat.to_csv( "C댓글_5.csv", index=False )
dat.to_excel( "C댓글_5.xlsx", index = False )

## 파일 읽기 함수 - open()
f = open("C댓글_5.csv", encoding='utf-8')
text = f.read()
print(text)