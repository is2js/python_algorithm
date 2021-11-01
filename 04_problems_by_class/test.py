# 느낀점:
# *1. 배열내 같은 것의 갯수를 위해 sort를 해놓고 확인한다.
# *2. set()자료구조를 직접 이용하기보다는 -> if len(set()) 로 서다 종류만 확인한다.
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


def money():
    lst = sorted(list(map(int, input().split())))
    
    if len(set(lst))==1:
        return 10000 + lst[0]*1000
    if len(set(lst))==2:
        # aa b or  b aa -> 어떻게는 [1]의 위치에 같은 눈이 있게 된다.
        return 1000 + lst[1]*100
    return lst[-1]*100

print(money())


    
    
