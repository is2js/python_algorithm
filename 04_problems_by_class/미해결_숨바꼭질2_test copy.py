# 느낀점:
# https://rebas.kr/750
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################
import sys 
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())

# 5 17 -> 4 2  
# 입력 : 5 100000
# 답 : 19 4
# 입력 : 5 1000
# 답 : 11 2

MAX = 10**5 # 일차원이면 범위가 필요하다.
ck=[0]*(MAX+2)
# * 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.
# -> 최단거리도 필요하고, 그 최단거리= 그 level에서 최단거리로 걸리는게 또 있는지 물어봄. -> 나중에 level단위로도 끊어야한다.
# dis=[0]*(MAX+2) 
dis = 0
L=0
L_flag = -3333 # 특정 level을 돌면서 찾는게 아니라, 최단거리 찾을 때 flag만 넣어주고, 그 level까지 진행하면 될듯하다.
cnt = 0 # 그 level까지 진행을 하긴하는데, 최단거리 또 나올때마다 cnt+=1해주면 될 것 같다.


dq = deque([5])
ck[5] = 1
# dis[5] = 0

# level단위로 끊기위해 바깥에 level단위로 쓸 반복문(무한루프)를 돌린다.
while True:
    # 최단거리 발견시 -> <넣기직전 자체처리>에서 flag에 표시를 해서, flag on일 때,  끊자. 
    if L==L_flag +1:
        break 

    # 여기 반복문은 level단위 전체실행이다.
    size = len(dq)
    for i in range(size):
        curr_level_node = dq.popleft()

        if curr_level_node == K: 
            # L_flag=True
            # break는 없다. level단위 끝까지 돌고, 바깥 반복문에서 탈출
            cnt+=1
            if L_flag == -3333 :
                L_flag=L
                print(L_flag, L)

        for next_level_node in (curr_level_node-1, curr_level_node+1, curr_level_node * 2):
            # 좌표이동시 1) index검사 2) ck검사
            if not (0<=next_level_node<=MAX):continue 
            
            if  (ck[next_level_node]):continue 

            dq.append(next_level_node)
            ck[next_level_node] = 1
            # dis[next_level_node] = dis[curr_level_node] + 1
    # dis+=1
    L+=1
# print(dis[curr_level_node])
print(L-1)
print(cnt)
#print(dis[:curr_level_node])











# ================최단거리 찾는 것으로만.... level 단위로 끊어볼려했었음..============
# if N==K:
#     print(0)
#     print(1)
#     exit()

# from collections import deque 
# MAX = 100000
# ch, dis = [0]*(MAX+2), [0]*(MAX+2)

# dq = deque([N])
# ch[N], dis[N] = 1, 0

# finish_level=False
# cnt=0
# while dq:
#     curr = dq.popleft() 
#     # print(dq, finish_level)
#     if curr == K :
#         # print("get")
#         # break
#         # * 나오자마자 멈추면 안되고, 최초발견level(거리)에서 똑같은 최단거리를 낸 방법이 있는지 해당레벨 전체를 다 봐야한다. (담레벨 직전까지)
#         cnt +=1
#         # *여기서 세지말고.. 재방문여부 체크란쪽에서 세보자?
#         if not finish_level:
#             finish_level = dis[K]
#     # print(finish_level)
#     if finish_level and dis[curr] == finish_level+1:
#         break

#     for next in (curr-1, curr+1, curr*2):
#         if not (0 <= next and next <= MAX):
#             continue
#         # * 방문여부로 건너띄기전에.. 같은놈 나왔으면 카운터 한번 세주자..
#         # if next == K:
#         #     # print("get K")
#         #     cnt+=1

#         if ch[next]:
#             continue 
        
#         dq.append(next)
#         # ch[next] = 1
#         dis[next] = dis[curr] + 1

# # print("ch :>>", ch[:30])
# # print("dis :>>", dis[:30])
# print(dis[K])

# print(cnt)