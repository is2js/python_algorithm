################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input == sys.stdin.readline
######################################################
k = int(input())

from collections import deque


for _ in range(k):
    N, M = map(int, input().split())
    prec = list(map(int, input().split()))
    docs = [ (pos, val) for pos, val in enumerate(prec) ]
    dq = deque(docs)
    cnt = 0

    if len(dq)==1:
        print(1)
        continue 

    while dq:
        temp = dq.popleft()
        if any(temp[1] < item[1] for item in dq):
            dq.append(temp)
        else:
            cnt +=1
            if temp[0] == M:
                print(cnt)
                break




