# bs4 -> naver 삼성전자 html dl태그 -> dd태그  -> 내부 한글 추출해보기
import requests
from bs4 import BeautifulSoup

base_url = "http://finance.naver.com/item/main.nhn?code=005930"
response = requests.get(base_url)
html = response.text

import re
stock_lst = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)",html)

result = re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", stock_lst[0][1])

print(*[x[1].split() for x in result], sep="\n")
