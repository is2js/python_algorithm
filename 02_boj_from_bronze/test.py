# 느낀점 : https://velog.io/@minzz/BOJ-1018%EB%B2%88-%EC%B2%B4%EC%8A%A4%ED%8C%90-%EB%8B%A4%EC%8B%9C-%EC%B9%A0%ED%95%98%EA%B8%B0-Python
# 1. 창의 갯수만큼, 각 창의 start_index를 row, col별로 돌아준다.
# 2. 체스판의 패턴배열은 i+j가 | 대각선을 형성하며, 이것들이 값이 다 0,0기준으로 일정하다.
# 3. 정답이 2개일 수 있따면, 각각 카운터해서 한번더 비교해야한다.

################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################
N = int(input())

data = [ int(input()) for _ in range(N)]
for x in sorted(data):
    print(x)

