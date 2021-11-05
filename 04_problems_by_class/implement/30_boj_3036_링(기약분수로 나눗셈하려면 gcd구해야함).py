# 느낀점:
# 1. 기약분수 나누기를 하려면, gcd 최소공배수를 각각 나눠줘야함.
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################


N = int(input())
data = list(map(int, input().split()))
a = data[0]
others = data[1:]

import math
gcd = math.gcd(a, b)

for b in others:   
    print(f"{a//gcd}/{b//gcd}")