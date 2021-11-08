# 느낀점:
# *1. itertools combinations, permutiations 말고도, -> math 모듈에 nCk를 계산하는 math.comb 와   factorial을 계산해주는 math.factorial as f 도 있다.
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