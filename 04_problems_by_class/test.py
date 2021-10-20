# 느낀점: 

################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# 단계별로 푸시는 분: https://developer-ellen.tistory.com/33 # 고민 많이 하시는 분이라 챙겨놓음.
######################################################
import sys

n = int(input())

data = [ int(input()) for _ in range(n)]
# print("data :>>", data)

import heapq as hq

hq_list = []
for x in data:
    if x!=0:
        hq.heappush(hq_list, -x)
    else:
        if hq_list:
            print(-hq.heappop(hq_list))

        else:
            print(0)
