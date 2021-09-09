from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = "https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC"
req = Request('url', headers={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()

print(url)