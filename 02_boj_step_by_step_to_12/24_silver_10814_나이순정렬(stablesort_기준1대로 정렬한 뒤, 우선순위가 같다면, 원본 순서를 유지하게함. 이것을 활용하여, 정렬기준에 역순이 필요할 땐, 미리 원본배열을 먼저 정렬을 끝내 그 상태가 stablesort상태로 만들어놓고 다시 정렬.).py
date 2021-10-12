"""
author : ChoJaeSeong
github : https://github.com/is2js
e-mail : tingstyle1

title : 나이순 정렬
description : 정렬
"""
# 참고사이트 : https://codingdog.tistory.com/604
# 느낀점 : python은 원래 stable sort를 사용하므로
# - 정렬기준 여러개 중에, 그렇지 않다면 [원래배열순서]를 그대로 유지하는 옵션이 자동으로 붙는다.
# - 정렬기준에 lst자체를 준다던가, x[1]을 다른 요소를 주면 오름차순 정렬하는 것이기 때문에 [원본 순서]는 지정할 수 없다.
# **정렬기준1로 정렬된 상태에서, 같은 우선순위라면, 원본의 순서를 유지시켜줌**
# **이것을 활용하여, 정렬기준에 역순이 필요할 땐, 미리 원본배열을 먼저 정렬을 끝내 그 상태가 stablesort상태로 만들어놓고 다시 정렬해도 된다.**
# sorted( : x[1]) : 이상태가 아래 정렬에 있어서는 stable_sort상태가 됨.
# sorted( : x[0], reverse=True)
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### input() == sys.stdin.readline()
### print() == sys.stdout.write(   + '\n')
######################################################
N = int(input())

data = [ input().split() for _ in range(N)]
data.sort(key=lambda x:(int(x[0])))
for element in data:
    print(' '.join(element))