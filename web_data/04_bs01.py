from bs4 import BeautifulSoup
from urllib.request import urlopen

page1 = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
</div>
<div>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역1] 필요없는 정보1 </p>
    <p class="p3"> [영역1] 필요없는 정보3 </p>
    <p id="p4"> [영역1] 필요없는 정보2 </p>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크 </p>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크222 </p>
    <p id="p4"> [영역2] 간단한 나의 홈페이지를 만들다.</p>
</div>
</body>
</html>
'''

#
#soup1 = BeautifulSoup(page1, 'lxml')
#print( soup1.title )

##
#one_info = soup1.find_all("div")
#print(len(one_info) )

soup1 = BeautifulSoup(page1, 'lxml')
wanted_info = soup1.find_all('div')[3]
print(wanted_info)
last_info_multi = wanted_info.find_all('p', class_="p3")
print(last_info_multi)

for one in last_info_multi:
    print(one.text)

wanted_info = soup1.find_all('div')[2]
last_info_multi = wanted_info.find_all('p', class_='p3')
a= []
for one in last_info_multi:
    #print(one.text)
    a.append(one.text)

print(wanted_info.children)
print(list(wanted_info.children)[9] )# children은 자기보다 한단계 낮은 레벨

### 전체를 가져오고 len으로 몇개인지 확인 후 for 문으로 돌려보기
# soup1 = BeautifulSoup(page1, 'lxml')
# wanted_info = soup1.find_all('div')
# print(len(wanted_info))
#
# for idx, one in enumerate(wanted_info):
#     print(idx)
#     print(one)


