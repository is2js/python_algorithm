# 느낀점:
# *1. math.comb는 pypy3으로 제출하면 runtime에러남.
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################

import math 

def construct_bridge():
    N, M = map(int, input().split())
    return math.comb(M, N)

for _ in range(int(input())):
    # 순서를 가짐 -> 뽑기만 하면 자동 순서배정
    res = construct_bridge()
    print(res)