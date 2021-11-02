# 느낀점:
# 풀이 참고: https://rebas.kr/750
# * 결론: 동일level 추가 최단거리 cnt는 queue에서 꺼내서 하니, ck 검사를 안하는 대신, queue에 넣는 조건을  <  if not dis[next]  + or  dis[next]==dis[curr]+1 >
#  -> 이미 최단거리가 발견되어 차있더라도, 그 level이 next의 level과 동일하면 같은 선상에서 발견된 것 -> queue에 넣어 cnt+1되도록 하자.
# * 1. level단위 실행시에는 L=0 L+=1 이 필요하다. 맨마지막에 L-=1번도 ..(분수찾기이후.. while 검사 변수cnt 업데이트 이후,,, 또 업데이트했기 때문에 하나 더 차있는 것!)
# * 2. cnt변수를 <큰 단위 by len(dq) -> 그만큼 while > 반복실행시에는 <cnt+1로 매겨진 순간부터 단위까지만 반복되도록> flag로써도 사용할 수 있다.
# * while not cnt:  cnt=0을 유지하는 동안만... cnt+=1직전까지.... 
# ** 근데 그 직전이.. 단위로 실행되서.. [  cnt=0--------cnt+=1되는 순간---------- 그 단위(level)의 끝] 으로서
# ** 딱 그 level까지만 진행된다. 대신. L+=1 업데이트는 계속 일어나므로 (검사변수 업데이트 이후 업데이트) -> 직전레벨로 한번 따로 돌아가줘야한다.
# * 3. 갯수만큼 돌도록 countdown by while ->  [while size: size -=1 ]: 0이 되기직전까지. -> n붙 1까지
# -> 다른 방법으로서 [n=0부터 내부에서 사용하면서 update하도록 시작 while n < N:  내부n활용 / n+=1 ]-> 0부터 N-1까지 -> N번
# * 4. 목표좌표 확인 및 cnt+=1는 queue에서 꺼낸 것을 확인 & 센다.
# * 5. 전설의 로직: if not dis[next] 비었거나 < or 차있더라도 > dis[next] 차있는 level이   dis[curr]+1 현재next의 level과 동일 선상에서 채워졌을 때 -> 같은 선상이라 queue에 넣는다.



################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################
import sys 
#sys.setrecursionlimit(10**8)
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())

MAX = pow(10,6)
dis = [0]* (MAX+2)
# *삭제1. 최단거리 1개만 구할건 아니다? 한 level에 여러개의 최단경로가 있을 수 있으니 <지나간 경로도 다시 한번 가면서> 다른경로도 다 지나야한다.
# ck = [0]* (MAX+2)
dq = deque([N])

# 추가1. 최단경로 = 최초발견level의  level전체에서, 목표좌표K가 발견될때마다 cnt+=1해야한다.
L = 0
cnt = 0

# *추가2. 
# * < while True -> if level변수 == 원하는 레벨: break -> level단위 실행 >해도 되겠지만 
# * < while flag로서 cnt변수에 +1 이 채워지기 직전까지만 돈다. while not cnt> -> level단위로 도니 채워지는 순간의 해당 최단거리level을 다 돌고 빠져나온다.
while not cnt: # [무한반복 & break & 특정레벨까지만 bfs]를 한번에..
    # 내부에서는 level단위로 실행시킨다.
    size = len(dq)
    while size: # *sense) 갯수 count다운을 while문으로!  n ... 0직전까지 -> 1까지..
        size-=1 # while문은 들어오느냐 못오느냐 차이지.. 어디서든 update해도 상관없은니 바로 하기
        curr = dq.popleft()
        # *로직 2: 
        # <BFS는 1개식 뺐을 때, 확인 >및 자체 처리를 한다?
        if curr == K:
            # 최초로 cnt가 올라갔지만, while은 level단위로 돌기 때문에, 목표좌표가 발견된 다음레벨에서 끝난다.
            cnt+=1
        
        for next in (curr-1, curr+1, curr*2):
            # 이동한 좌표의 index로서 검사
            if not ( 0<= next <=MAX): continue 
            
            # *로직3: ck검사는 없다. 자식이 이미 나왔던 거라도 중복되더라도 좌표를 다 돌아야지만, tree가 목표level을 다 그릴 수 있다.
            
            # *로직4: ck없이 돌고있으니, (ck가 있었으면, 자식이 아직 미방문이니 무조건 dis[자식]= 자식의 최단거리 를 채워줬었다.)
            # * -> dis[자식좌표]가 <아직 자식놈의 최단거리 미방문>으로 해당좌표의 최단거리(level)가 비어있거나  <--늦게 발견된 놈이 덮어씌우면 안됨! (덮쓰방지!)
            # * -> or [   ]로서.. 앞에께 False라서 이미 dis[자식] 차있는 경우라도?
            # * -> 이미 다른 곳에서 최단거리를 채웠더라도.., 그 채워져있는 값이 , <현재자식level인 dis[curr]+1>과 동일한 레벨로 채워져있다??
            # * --> 같은 level이다. < queue에넣어서 -> 뽑힐 때 cnt 되도록 하자!!!> 
            # * ---> my) 만약, cnt용으로만 넣더라도.. 
            # cf) if not은 괄호 안붙이면 그냥 바로뒤엣것만 인식됨. 

            # 요약) ck대신.. dis[]가 비었거나, 차있더라도 현재level+1으로서, [차있는 level == 현재 자식level 과 같은 수준]이면 -> cnt되어야한다. 넣어서, 다음루프에 빼서 cnt+=1시키도록 넣어준다.
            if not dis[next] or dis[next] == dis[curr]+1:
                
                dq.append(next)
                # * 로직 5: queue에 넣는 것과 동시에.. dis[자식]도 채워야함. -> 뒤 조건은 공통이긴 한데 그래도 채워줌
                dis[next] = dis[curr]+1

    L +=1

# *로직5: cnt가 0에서 도는 중간 flag로 작동해 1단계 올라간 다음 level에서 종료 -> slevel도 한단계 +1없데이트 된 상태로 종료되니. 한번 -1 해줘야한다.
L-=1 

print(L)
print(cnt)


            




        






# =========================또 실패, 최단거리와.. 체크표시와... 해당level동안 실행...
# 5 17 -> 4 2  
# 입력 : 5 100000
# 답 : 19 4
# 입력 : 5 1000
# 답 : 11 2

# MAX = 10**5 # 일차원이면 범위가 필요하다.
# # ck=[0]*(MAX+2) # 1. 일단 체크변수가 없어야한다? 이미 지나갔가서 생략된 것 중에서도 ->  최단level에서 등장할 수 있어서?
# # * 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.
# # -> 최단거리도 필요하고, 그 최단거리= 그 level에서 최단거리로 걸리는게 또 있는지 물어봄. -> 나중에 level단위로도 끊어야한다.
# dis=[0]*(MAX+2) 
# dis = 0
# L=0
# L_flag = -3333 # 특정 level을 돌면서 찾는게 아니라, 최단거리 찾을 때 flag만 넣어주고, 그 level까지 진행하면 될듯하다.
# cnt = 0 # 그 level까지 진행을 하긴하는데, 최단거리 또 나올때마다 cnt+=1해주면 될 것 같다.


# dq = deque([5])
# ck[5] = 1
# # dis[5] = 0

# # level단위로 끊기위해 바깥에 level단위로 쓸 반복문(무한루프)를 돌린다.
# while True:
#     # 최단거리 발견시 -> <넣기직전 자체처리>에서 flag에 표시를 해서, flag on일 때,  끊자. 
#     if L==L_flag +1:
#         break 

#     # 여기 반복문은 level단위 전체실행이다.
#     size = len(dq)
#     for i in range(size):
#         curr_level_node = dq.popleft()

#         if curr_level_node == K: 
#             # L_flag=True
#             # break는 없다. level단위 끝까지 돌고, 바깥 반복문에서 탈출
#             cnt+=1
#             if L_flag == -3333 :
#                 L_flag=L
#                 print(L_flag, L)

#         for next_level_node in (curr_level_node-1, curr_level_node+1, curr_level_node * 2):
#             # 좌표이동시 1) index검사 2) ck검사
#             if not (0<=next_level_node<=MAX):continue 
            
#             if  (ck[next_level_node]):continue 

#             dq.append(next_level_node)
#             ck[next_level_node] = 1
#             # dis[next_level_node] = dis[curr_level_node] + 1
#     # dis+=1
#     L+=1
# # print(dis[curr_level_node])
# print(L-1)
# print(cnt)
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