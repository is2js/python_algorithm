# https://www.google.com/googlebooks/uspto-patents-grants-text.html

# zip파일 url 중간에 grant(특허등록) 문자열이 포함되어 있는 것만 추출하기
import re 
with open('./zip_files_in_html.txt', 'r', encoding='utf-8') as f:
    string = f.read()
    # findall은 소괄호 안치면 그부분이 추출이 아예 안되니, 나눠서 받더라도 다 포함되도록 해보자.
    # 내부에 포함 -> sql like처럼 앞뒤에 문자반복되도록 걸어준다. (.+)(grant)(.+)
    url_list = re.findall('(http)(.*)(grant)(.*)(\.zip)', string)

url_list =  [ ''.join(x) for x in url_list ]
url_list