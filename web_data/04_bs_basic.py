from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"

page = urlopen(url) #웹url로부터 페이지를 가져옴
print(page)

page = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
<a href="https://www.naver.com/">naver</a>
<a href="https://www.google.com">google</a>
<img height="300" src="dog_01.jpg" width="500"/>
<p> 내가 가장 좋아하는 동물은 강아지입니다.</p>
<p> 나는 그리고 네이버 홈페이지에 자주 갑니다.</p>
<p class="p3"> 강아지 사진과 네이버 링크 </p>
<p id="p4"> 간단한 나의 홈페이지를 만들다.</p>
<p class="p3"> 강아지 사진과 네이버 링크222 </p>
</div>
</body>
</html>
'''
## HTML Parse란 html문법 규칙을 따른 문자열을 다른 문법을 기준으로 단어의 의미나 구조를 분석하는 것을 말함
## 이를 수행하는 프로그램을 HTML Parser라고 함(lxml(c로 구현된 가장 빠름), html5lib, html.parser)

soup = BeautifulSoup(page, 'lxml')
print(soup.title)

# 태그명 soup.태그명 ==> 해당되는 요소읮 정보를 가져온다.
# print(soup.title) #첫번쨰
# print(soup.body) #처음부터 다
# print(soup.div)
# print(soup.img)
print(soup.a)
print(soup.a.text) ## >....</a> 꺽쇠사이의 text를 가져옴
print(soup.div.p.text)

#id, class을 활용해서 정보가져오기 - 하나의 요소 (find)
#id, class을 활용해서 정보가져오기 - 모든 요소 (find_all)

print(soup.find("p", id = "p4").text)
print(soup.find_all("p"))
# find, find_all
# naver 정보
print(soup.find("a").text)
# 모든 a태그 정보 가져오기
print(soup.find_all("a"))

print ()
a1 = soup.find("a")
print(type(a1), a1.text)

a=soup.find_all("a")
print(type(a),a[1].text)

##실습 2-3
##한 줄코드
##class 정보를 이용해서 p3인 것을 가져와서 2번째 요소의 text를 가져와보자
data1 = soup.find_all("p", class_="p3")[1].text
print(data1)
##<p class="p3"> 강아지 사진과 네이버 링크 </p>
print(soup.find_all("a")[1].text)

