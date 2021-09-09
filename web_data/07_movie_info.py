from bs4 import BeautifulSoup
from urllib.request import urlopen

# url 정보
# tag 정보, id, class 정보
url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
tit_data = soup.find("dt", class_="tit").find("a").text
# print(tit_data)

tit_all_data = soup.find_all("dt", class_="tit")

list_all = []
for one in tit_all_data:
    title_one = one.find("a").text
    list_all.append(title_one)
# print(len(list_all), list_all)
print(list_all)
# score_all = soup.find_all("span", class_="num")
# print(score_all[1].text)

# 스코어 점수
score_all = soup.find_all("dl", class_="info_star")
# print(score_all[2].find("span", class_="num").text)
all_score = []
for one in score_all:
    one_score = one.find("span", class_="num").text
    # print(one_score)
    all_score.append(one_score)
print(all_score)

# 예매율 정보 가져와보기

rate_tmp = soup.find_all("dl", class_="info_exp")
rate_all_all = []
for one in rate_tmp:
    one_rate = one.find("span", class_="num").text
    # print(one_score)
    rate_all_all.append(one_rate)
print(rate_all_all)

#참여명수
num_all_info = soup.find_all("dl", class_='info_star')
# num_people = soup.find_all("em")

num_all = []
for one in num_all_info:
    one_data = one.find("em").text
    num_all.append(one_data)

print("참여 명수 ", num_all)

# 타이틀, 평점, 평점 참여명수 , 예매율
# 파일 만들기
import pandas as pd
# list_all, all_score, num_all
dict_dat = {"영화제목":list_all,
            "평점":all_score,
            "평점 참여명수":num_all}
dat = pd.DataFrame(dict_dat)
print(dat)
dat.to_csv("naver_movie_info.csv", index=False) # index 숫자 넣을지 말지
dat.to_excel("naver_movie_info.xlsx", index=False)