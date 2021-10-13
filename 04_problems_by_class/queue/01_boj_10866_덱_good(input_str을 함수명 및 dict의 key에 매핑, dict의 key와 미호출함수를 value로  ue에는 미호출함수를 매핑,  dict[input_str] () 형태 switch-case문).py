# 느낀점:
# 1. input_str -> def [함수명]()정의 및 dict의 [key] = value에는 미호출함수 매칭. -> dict[input_str] () 형태로  def input_str()함수를 호출만 하면됨.
# -> 그로 인해 if input_str: dict[input_str] () 호출로 꺼내쓸 수 있다.
# -> 여태껏, list hash, count 정렬 : n범위과 index를 매칭시켜 val로 표시
# -> this: input문자열 -> [함수명]과 매칭 및 [dict의 키]로 매칭 미호출 함수명을 매핑
# **TODO: dict 를 활용한 switch-case**
# **cmd_dict[cmd] : 자체가 cmd미호출 함수 -> dict[key]()형태로 호출만 하면된다.

################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input == sys.stdin.readline
######################################################
n = int(input())
from collections import deque

dq = deque([])

# 0. input문자열을 함수명으로 정의함
def push_back(dq, x):
    dq.append(x)

def push_front(dq, x):
    dq.appendleft(x)

def pop_front(dq):
    if dq:
        dq.popleft()
    else:
        print(-1)
def pop_back(dq):
    if dq:
        dq.pop()
    else:
        print(-1)

def size(dq):
    print(len(dq))

def empty(dq):
    if dq:
        print(0)
    else:
        print(1)

def front(deq):
    if deq:
        print(deq[0])
    else:
        print(-1)

def back(deq):
    if deq:
        print(deq[-1])
    else:
        print(-1)


# 1. input문자열을 함수명 및 dict의 키에 매칭
# - dict의 key에 호출직전의 함수를 넣어놓는다. dict[key]()형태로 호출만 하면된다.
cmd_dict = {
'push_back' :  push_back, 
'push_front':push_front,
'front':front,
'back':back,
'size':size,
'empty':empty,
'pop_front':pop_front,
'pop_back':pop_back,
}

# 2. input문자열을 받아서, dict에서 key로 해당함수를 꺼낸 뒤, 호출한다.
for _ in range(n):
    statement = input().split()
    # list

    cmd = statement[0]
    # cmd_dict[cmd] : 자체가 cmd미호출 함수 
    # -> dict[key]()형태로 호출만 하면된다.
    if len(statement) > 1:
        k = statement[1]
        cmd_dict[cmd](dq, k)
    else:
        cmd_dict[cmd](dq)
    




# 내 풀이
# for _ in range(n):
#     cmd = input().split()
#     if len(cmd) > 1:
#         k = int(cmd[1])
#     else:
#         cmd = cmd[0]

#     if cmd == "push_back":
#         dq.append(k)
#     elif cmd == "push_front":
#         dq.appendleft(k)
#     elif cmd == "pop_front":
#         if dq:
#             print(dq.popleft())
#         else:
#             print(-1)
#     elif cmd == "pop_back":
#         if dq:
#             print(dq.pop())
#         else:
#             print(-1)
#     elif cmd == "size":
#         print(len(dq))
    
#     elif cmd == "empty":
#         if len(dq) == 0:
#             print(1)
#         else:
#             print(0)
        
#     elif cmd == "front":
#         if dq:
#             print(dq[0])
#         else:
#             print(-1)
#     elif cmd == "back":
#         if dq:
#             print(dq[-1])
#         else:
#             print(-1)
    
    
