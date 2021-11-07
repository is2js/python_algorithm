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

# nCk = n! / k! (n-k)!     n /n-k     n-1! / k! (n-1 -k) n-1Ck
# n
# from math import factorial as f
# n, k = map(int, input().split())
# print(int(f(n)/(f(n-k)*f(k))))

# import math
# print(math.comb(*map(int,input().split())))
import math 
N, K = map(int, input().rstrip().split())

print(math.comb(N,K) % 10007)