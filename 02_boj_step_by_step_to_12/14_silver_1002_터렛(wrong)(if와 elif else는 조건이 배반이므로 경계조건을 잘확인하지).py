# 느낀점 : 
# - 두점사이의 거리에서 두점이 0이 되는 경우는 완전히 따로 빼준다.(생각함)
# - 직접 값을 안구해도되고  두 수의 차이만 구하고 싶을 땐 abs(r1 -r2)로 해결한다.
# - if elif else 는 완전히 배반인 경우다. if에서도 잘 나누자.
# - r1+r2 == l 일때 1점이되었따가. r1+r2 > l부터 2점으로 들어오지만
# **들어는 마지노선도 있다. l == abs(r1-r2)의 1점되는 것이 마지노선이니.. 그 마지노선보다..l이 커서 2점으로 삐져나갈 것!!!!!!!!!!**
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################
N = int(input())

import math 

def distance(tuple_list):
    x1, y1= tuple_list[0]
    x2, y2= tuple_list[1]

    return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))


# 1. 0점 -> 1점 -> 2점 -> 안에서 1점 -> 안에서 0점 -> 안에서 무한대?
# -------------
# 0)  두점이 같은 위치..  r1=r2 : 무한대
# 0-2) 두점이 같은 위치.. r1 !=r2 : 0
# -------------
# 1) r1+r2 > l : 2점
# 2) r1+r2 == l : 1점  / r1 + l == r2 : 1점
# 3) 그외 0점

for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = r1+r2
    r_min = min(r1,r2)
    r_max = max(r1,r2)

    l = distance([(x1,y1), (x2,y2)])
    # print(x1, y1, r1, x2, y2, r2)

    # 두점 사이의 거리가 중요한데, 두점이 같을 경우는 완전히 따로빼서 관리하자.
    if l == 0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        if r < l:
            print(0)
        elif r == l or l == abs(r1-r2):
            print(1)
        elif r > l and l > abs(r1-r2):
            print(2)
        else:
            print(0) 

