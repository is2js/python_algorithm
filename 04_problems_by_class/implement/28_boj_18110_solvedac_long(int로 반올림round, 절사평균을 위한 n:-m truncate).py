# 느낀점:
# * 1. 반올림을 math.floor, ceil없이 [int() + 삼항연산자]로 더 쉽게 구할 수 있다.
#   1-1. 정수부분int(n) 따로 / 소수부분을 구하고 삼항연산자로 +0 or +1
# -> return  int(n) + (1 if n-int(n) >=0.5 else 0)
# * 2. 30% 절사평균 -> 앞15% 뒤 15% truncate -> 
# * 앞 k개 제외 -> [k:]
# * 뒤 k개 제외 -> [:-k]  == [:n-k]
# **          -> 전체 :n으로 n-1까지니까 -> 1개 제외 :n-1   2개:n-2,   k개:n-k로도 할 수 있다.
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################
def normal_round(n):
    return int(n) + (1 if n - int(n) >= 0.5 else 0 )

lst = [int(input()) for _ in range(int(input()))]

if not lst:
    print(0)
    exit()
if len(lst) == 1:
    print(lst[0])
    exit()

lst.sort()


m = normal_round(len(lst) * 0.15)
lst = lst[m:-m]
print(normal_round(sum(lst)/len(lst)))