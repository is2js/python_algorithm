# 느낀점 : 
# 1. 반복횟수가 나올 땐, 각 input을 comp로 반복횟수만큼 동시에 받자.
# 2 . 각 item에 대해, 속해있는 그룹 전체를 다시 돌면서 비교, for + list(filter(lambda x: x,item ))
#    - filter(lambda:에서 [도는x]과 [각item]으로 만난다,     전체그룹)
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################
N = int(input())
items = [ list(map(int, input().split())) for _ in range(N) ]

print(items)

answer = []

for item in items:
    answer.append(
        len(list(filter(lambda x: x[0] > item[0] and x[1] > item[1] , items))) \
            +1
    )

print(*answer)


# items_info = [1]*len(items)

# for idx, (x,y) in enumerate(items):
#     for idx2, (p,q) in enumerate(items):
#         if idx != idx2 and x<p and y<q:
#             items_info[idx] += 1

# print(*items_info)


