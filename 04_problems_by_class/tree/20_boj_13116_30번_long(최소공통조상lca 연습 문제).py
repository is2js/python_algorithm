# 느낀점:
# https://www.acmicpc.net/problem/2667


################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################
import sys 
input = sys.stdin.readline

def process():
    A, B = map(int, input().split())
    
    Aa, Ba = [], []
    Ad, Bd = 0, 0

    while A != 1:
        Aa.append((A, Ad))
        A //= 2
        Ad += 1
    Aa.append((A, Ad))

    while B != 1:
        Ba.append((B, Bd))
        B //= 2
        Bd += 1
    Ba.append((B, Bd))

    for x in Aa:
        for y in Ba:
            if x[0]==y[0]:
                return x[0]

    return None

    


for _ in range(int(input())):
    # 
    ret = process()
    print(ret*10)

