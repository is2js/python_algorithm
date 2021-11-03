# https://www.randomlists.com/phone-numbers

import re 
# p = re.compile('010\-[0-9]{4}\-[0-9]{4}')
p = re.compile('02\-[0-9]{4}\-[0-9]{4}')

# 전화번호부 추출해보기
# re.compile, p.match if m 
with open('./telephone.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines() # line = \n별로 끊어진 문자열list가 들어온다.
    # print(string)  # 'ABC\t201511111\t010-0000-7924\tadfdasf\n'
    # 1. list가 아니라 각 문자열을 줘야하며
    for line in lines:
        # 2. 정확하게 패턴이 있는 곳만 끊어서 줘야. 있냐/없냐?를 판단한다. line 전체를 줄 때 못찾는다.
        # m = p.match(line)
        try:
            # 해당 인덱스가 없는 line일 수도 있다.
            m = p.match(line.split('\t')[2])
        except:
            continue
        if m: print(m[0])

