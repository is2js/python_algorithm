# 느낀점:
# 1. sys.exit()로 반복문 아니라도 break 로직종료가 가능하다.
# 2. deque에는 .rotate()함수가 있어서 원형큐처럼 사용이 가능하며, 기본적으로 right rotation이다.
# 3. deque에는 .index()함수도 있어서 굳이 for문으로 찾아다닐필요없다.
# 4. 전진횟수 = index차 -> 어느쪽으로 회전? 전진? -> n//2포함 기준 같거나 작으면, 그대로 -> 크면 거꾸로 전진횟수 세기
# **0에서 거꾸로 전진횟수 = 012345,0=6=len이라 생각하고 index차이로 구한다.**
# <뒤로 전진횟수도 index-index로 하면된다. 대신 0을 맨 뒤에 놓고, 그 index는 6으로 본다.>
# ex> 0에서 4까지는 뒤로 몇칸?   4 5 0(6)   0-4 = 6-4 = len - index
# 5. 반을 나눠 -> 우측거리, 좌측거리 둘중에 어느쪽이 가까운지는 if else의 삼항연산자를 활용해서 한줄표기가 가능하다.
# my) 전진횟수 = 두 index의 차이
# 6. 반복문 + if종착역: break  /  정해진 반복문 + if 건너뜀: continue
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input == sys.stdin.readline
######################################################
from collections import deque

n, m = map(int , input().split())
dq = deque(range(1, n+1))
# print(dq)
# print(dq.index(3)) # 0 -> 2 : index자체가.. 0번index에서부터 2번 전진
# ---♥--n//2---- 0~절반(혹은 절반왼쪽)까지는 좌측회전 : dis = index(3)-0
# ----n//2---♥-- 절반+1 ~n까지는 우측회전 : dis = len(10)-index(8)
# 01[2]345 -> n//2: ->[2] ->  2-0:2칸전진
# 0123[4]5 -> n//2: ->[2] -> [4]50 -> [4]56 -> len-index = 6-4: 2칸 전진

pos_list = map(int, input().split())

count = 0 

for pos in pos_list:
    print(pos, dq)
    # 3. dq.index()의 검색을 쓰기도 전에, [0]인덱싱으로 먼저 가지치기한다.
    if dq[0] == pos:
        dq.popleft()
        continue
    # 1. 찾는 수를 dq.index()로 인덱스를 구하낟.
    index = dq.index(pos)

    # 2. index를 알면, 0번 index 에서부터의 전진횟수를 찾을 수 있다. 거꾸로도 전진할 수 있으니 n//2기준으로 판단한다
    if index <= (len(dq)//2):
        dis = index - 0
        # 3. dq.rotate는 기본적으로 우회전(시계방향)=뒤에것빼서 앞에 붙임. 
        # -> 왼쪽으로 땡기려려면(앞에것빼서 뒤로), -를 달아야한다.
        dq.rotate(-dis)
    else:
        dis = len(dq) - index  # 이 경우는 rotate를 꺼꾸로 해야함.
        dq.rotate(dis)
    
    
    dq.popleft()
    count+=dis
    #print(pos, dq, dis, count)

print(count)


    








# 내풀이 (틀림)
# n, m = map(int , input().split())
# pos_list = list(map(int , input().split()))

# dq = deque(list(range(1, n+1)))

# def left_rot(dq):
#     if dq:
#         dq.append(dq.popleft())
#     else:
#         raise IndexError

# def right_rot(dq):
#     if dq:
#         dq.appendleft(dq.pop())
#     else:
#         raise IndexError
    
# def find_nearest_num(dq, pos_list):
#     nearest_rot = 'l'
#     nearest_dis = len(dq)
#     nearest_val = dq[-1]
#     print(pos_list, dq)
#     for pos in pos_list:
#         # 0123  0과 2,  0과 3 -> 더가깝..
#         # -1 index = -1, -2 ... len(dq)= 3-4 , 2-4 index-len(dq)
#         #dis = min((dq.index(pos) - 0), abs(dq.index(pos)-len(dq)))
#         if (dq.index(pos) - 0 ) > abs(dq.index(pos)-len(dq)):
#             rot ='r'
#             dis = abs(dq.index(pos)-len(dq))
#         else:
#             rot='l'
#             dis = (dq.index(pos) - 0)
#         # print("dis>>>", dis)
#         if nearest_dis > dis:
#             nearest_dis = dis
#             nearest_val= pos
#             nearest_rot = rot
#             # print("교체...", nearest_rot, nearest_dis, nearest_val)
#     return nearest_rot, nearest_dis, nearest_val

        

# count = 0


# #print(find_nearest_num(dq, pos_list))
# # while dq and pos_list:
#     # nearest_rot, nearest_dis, nearest_val = find_nearest_num(dq, pos_list)
#     # print(nearest_rot, nearest_dis, nearest_val, dq, pos_list)
# for pos in pos_list:
#     print(dq, pos)
#     if dq[0] == pos:
#         dq.popleft()
#     else:
#         if (dq.index(pos) - 0 ) > abs(dq.index(pos)-len(dq)):
#             dis = abs(dq.index(pos)-len(dq))
#             rot = 'r'
#         else:
#             dis = (dq.index(pos) - 0)
#             rot = 'l'
#         for _ in range(dis):
#             if rot == 'r':
#                 right_rot(dq)
#             else:
#                 left_rot(dq)
#             count+=1
#             print(dis,count,rot)
#     #break
# print(dq)
# print(count)



