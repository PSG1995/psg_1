import wordcloud
from wordcloud import WordCloud, STOPWORDS
from matplotlib import rc #폰트를 지정해줌
print(wordcloud.__version__)

## 파일 읽기 함수 - open()
f = open("C댓글_5.csv", encoding='utf-8')
text = f.read()
print(text)
f.close()

rc('font', family = 'NanumGothic')

wcloud = WordCloud('./data/D2Coding.ttf',
                   max_words=1000,
                   relative_scaling=0.2).generate(text)
print(wcloud)
import matplotlib.pyplot as plt
plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear') # 손실되는 값을 어떻게 보완하고 처리할 것인가에 대한 방법
plt.axis('off')
plt.show()