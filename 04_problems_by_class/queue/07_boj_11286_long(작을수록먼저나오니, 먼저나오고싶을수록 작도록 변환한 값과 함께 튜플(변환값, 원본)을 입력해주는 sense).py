# 느낀점: 
# 1. 작은순으로 뽑을 게 아니라면, hq에는 튜플로 기준을 만들어서 넣어준다. (기준값자리로서 원하는 값일수록 작도록 변환값, 원본값) 튜플형태로 넣는다.
#   ex> [최대값] <우선>뽑도록 == [최대값]일수록 <작도록 변형>---> 마이너스 달기
#   ex> 원본유지안해되면(=원본값 복구가능하면) 튜플이 아닌 원본값을 변형해서 push -> 뽑고나서 복구
# 2. x에 [절대값 작을수록] <우선>뽑도록 == [절대값 작을수록] 작도록 변형 & 복구쉽지않으니 튜플로 변형해서 heappush
# 3. 있어서 뽑는다면, 알아서 변환된작은값 먼저 뽑혀 == 원하는 원본값부터 나오니, 출력할때 원본값 튜플 [1]요소를 출력
# * 변환값(기준값, 튜플[0])이 같다면?  원본값이 작을수록 먼저 나온다고 한다.
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
######################################################
import sys
input = sys.stdin.readline

n = int(input())

data = [ int(input()) for _ in range(n)]


import heapq as hq

q = []

for x in data:
    # 1. 작은순으로 뽑을 게 아니라면, hq에는 (원하는 값일수록 작도록 변환값, 원본값) 튜플형태로 넣는다.
    #   ex> [최대값] <우선>뽑도록 == [최대값]일수록 <작도록 변형>---> 마이너스 달기
    #   ex> 원본유지안해되면(=원본값 복구가능하면) 튜플이 아닌 원본값을 변형해서 push -> 뽑고나서 복구
    if x!=0:
        # 2. x에 [절대값 작을수록] <우선>뽑도록 == [절대값 작을수록] 작도록 변형 & 복구쉽지않으니 튜플로 변형
        x = (abs(x), x)
        hq.heappush(q, x)
    else:
        if q:
            # 3. 있어서 뽑는다면, 알아서 먼저 뽑히니, 원본값을 출력하도록 튜플 [1]요소를 출력
            print(hq.heappop(q)[1])
        else:
            print(0)
