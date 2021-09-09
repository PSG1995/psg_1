import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')

## 상영작/예정작 제목만 뽑기

movie_info = soup.find("ul", class_='lst_detail_t1').find_all("li")
print( len(movie_info) )
print( movie_info[122].find("dt", class_="tit").a.text  )
## 평점만 뽑기
print( movie_info[0].find("span", class_="num").text)
## 참여 명수
print( movie_info[0].find("em").text)
## 예매율
temp = movie_info[122].find("dl", class_="info_exp")

if temp is not None:
    t=temp.span.text
    print("값이 있음", t)
else:
    t=0
    print("값이 없음", t)

# print(one.find("dt", class_="tit").a.text)
## 개요
txt = movie_info[0].find("span", class_="link_txt").text
txt_last = txt.replace("\n", "")
txt_last = txt_last.replace("\t", "")
txt_last = txt_last.replace("\r", "")
print( txt_last )

# ## 감독
# director = soup.find(("dl", class_="info_txt1")."span", class_="link_txt")
# print(director)
# 제목, 평점, 참여수, 개요
all_title = []
all_score = []
all_people = []
all_category = []
all_rate = []

for one in movie_info:
    title = one.find("dt", class_="tit").text
    score = one.find("span", class_="num").text
    num = one.find("em").text
#예매율
    tmp = one.find("dl", class_="info_exp")
    if tmp is not None:
        rate = tmp.span.text
    else:
        rate = 0

    category = one.find("span", class_="link_txt").text
    txt_last = txt.replace("\n", "")
    txt_last = txt_last.replace("\t", "")
    txt_last = txt_last.replace("\r", "")


    all_title.append(title)
    all_score.append(score)
    all_people.append(num)
    all_rate.append(rate)
    all_category.append(txt_last)

print(len(all_title), len(all_score), len(all_people), len(all_category), len(all_rate))
dat_dict = {
    "제목":all_title, "평점":all_score, "참여명수":all_people, "예매율":all_rate, "개요": all_category}
dat = pd.DataFrame(dat_dict)
dat.to_csv("네이버영화.csv", index = False)
dat.to_excel("네이버영화.xlsx", index = False)