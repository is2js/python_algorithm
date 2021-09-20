# 느낀점 : 
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################

# 느낀점 : 
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################
# 느낀점

N= int(input()) # 그 당시(제일 큰)의 빈 행렬을 만들기 위해 받아놓고 바로 처리

# 

def hanoi(n, start, end):
    if n == 1:
        print(1, 3)

    hanoi(n-1, 1, 2)
    print(1, 3)
    hanoi(n-1, 2, 3)
    return 

