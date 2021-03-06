"""
author : ChoJaeSeong
github : https://github.com/is2js
e-mail : tingstyle1

title : 단어
description : 정렬
"""
# 느낀점 : 정렬기준을 2개 이상 줄 때, 오름차순이 보장되려면 자기자신x를 튜플에 넣어주면 된다.
# - sort(key=lambda x: (len(x), x )): 길이순+ 우선순위가 오름차순
# - 정렬해놓고 다시 list(set())하면 순서 엉클어진다.
# cf) 정렬기준1가 끝나면, python-내부stablesort로 인해, 우선순위 같은 나머지에 대해서 원본lst순서를 유지하게 한다.
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### input() == sys.stdin.readline()
### print() == sys.stdout.write(   + '\n')
######################################################
N = int(input())

data = [ input() for _ in range(N)]
data = list(set(data))

data.sort(key=lambda x:(len(x),x))


for x in data:
    print(x)
