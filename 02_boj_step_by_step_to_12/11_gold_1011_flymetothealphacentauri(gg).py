from input import Input

x, y = Input.data

# https://ooyoung.tistory.com/91

n = y - x

distance = x-y-2 # 중간에 n번을 구했으면  거기서 앞뒤 -1씩    +2 해줘야한다.

##  전진하는 경우의수의 경우, 
# 1. 출발점은 표기하지말자.
# 2. 화살표 없이 이어서 붙여서 규칙을 발견하자.
# **3. 규칙이 안보이는 것 같을 땐, 차이를 보자**

# 문제요구 : 작동횟수 최소 -> 이어진 숫자들이 짧을 것. -> 할 수 있다면, 1로 줄어들기전에 최대한 높이 올라갔따가 내려와야한다.
# 길이의 최소 -> 1시작으로 2부터 쭉쭉 올라가다가 1로 도착할 수있는지 최대한 length를 조금내려고하면서 만든다.
# 특징 : 문제가.. 2^k-1끝..
#1 :1 -> 1              루트(1)
#2: 11 -> 2             

#3 : 1 1  1 ->3         
#4 : 1 2  1 ->3         루트(4)-1

#5 : 1 21 1 ->4       
#6 : 1 22 1 ->4        

#7 : 1 221 1 -> 5     
#8 : 1 222 1 -> 5     
#9 : 1 232 1 -> 5      루트(9) = 3 +2

#10 : 1 2321 1 -> 6   
#11 : 1 2322 1 -> 6   
#12 : 1 2332 1 -> 6   

#13 : 1 23321 1 -> 7  1
#14 : 1 23321 1 -> 7  1
#15 : 1 23321 1 -> 7  1
#16 : 1 23321 1 -> 7  1   루트(16) = 4 

#An = 123344555666

#Bn =  1 1
#  Cn =  1  1  2  2  3  3    C2k-1 = k , C2k=k ->

# An = 1+ 시그마(Bn-1) (N>=2)   = 1+ 시그마() 



# yb1020의반올림 작전?
# import sys
# import math

# n = int(sys.stdin.readline())

# for i in range(n):
#     start, end = map(int, sys.stdin.readline().split())
#     dis = end - start
#     #sqr = math.sqrt(dis)
#     #move = round(sqr)
#     #if sqr - int(sqr) >= 0.5 or sqr == int(sqr):
#     #    print(2*move - 1)
#     #else:
#     #    print(2*move)
#     move = round(math.sqrt(dis))
#     if move**2 < dis:
#         print((2*move))
#     else:
#         print((2*move) - 1)
                



# new05 의 /2 + 올림작전?
import math
t = int(input())
l = [list(map(int,input().split())) for i in range(t)]
# k1=1 .... kn = 1
# (0,1,2) (1,2,3) ....
# 1 /  1 + 1 / 1 + 1 + 1 / 1 + 2 + 1 / 1 + 2 + 1 + 1
# 1 + 2 + 2 + 1 / 1 + 2 + 2 + 1 + 1
# 1 + 2 + 2 + 2 + 1 / 1 + 2+ 3 + 2 + 1
# 1 ~ 10 : 1 + 2 + 3 + 2 + 1 + 1 = 10
# 1 + 2 + 3 + 3 + 2 + 1 + 1 = 13
# 1 + 2 + 3 + 4 + 3 + 2 + 1 + 1 = 17
# 1 + 2 + 3 + 4 + 4 + 3 + 2 + 1 + 1 =21
# 1 + 2 + 3 + 4 + 5 + 4 + 3 + 2 + 1 + 1 = 26

# 1 / 2 / 3 / 5 / 7 / 10 / 13 / 17 / 21 / 26 / ....
# (1) (2) (3) (4) (5)....
# 1 1 / 2 2 / 3 3 / 4 4 / ....


# 1 ~ 20 : 1 + 2 + 3 + 4 + 4 + 3 + 2 + 1
# sigma(k) from 1 to n : n(n+1)/2
for i in range(t):
    lt = l[i][1] - l[i][0]
    n = 0
    h = 1
    while True:
        n += 1
        h += math.ceil(n/2)
        if h == lt:
            print(n+1)
            break
        elif h > lt:
            print(n)
            break