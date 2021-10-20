"""
author : ChoJaeSeong
github : https://github.com/is2js
e-mail : tingstyle1

title : 좌표 정렬하기
description : 정렬
"""
# 느낀점 : 배열의 n번째원소 기준으로 정렬은 쉽지만.. 2번째 정렬기준을 추가해야한다면..
# my) 1번째원소순으로 정렬시켜놓고,, for문을 돌면서, 1번째 원소가 같을 때, 2번째 원소를 비교하여, 다르면 swap하도록 함.
#    swap을 위해서는.. 좌표를 tuple이 아닌 list로 선언해야한다.
#    --> 실패: 정렬이라는 것은.. 해당 그룹(x값이 같은 모든 데이터들)다 모은 상태에서, 2개의 값만 연쇄적으로 비교하면 안된다.
#    --> 실패 예:  같 같 작 -> for문을 i-1, i만 비교시 =>  같 작<->같 의 정렬만 일어남.
#    --> 정렬이란.. 해당 그룹 전체 모은 상태에서 i항을 돌면서.. 삽입/선택/퀵정렬을 하자. 앞뒤로만 비교해선 안됨..
# **new)  sort()함수의 key=lambda에 정렬 2번째 기준을 이어진 튜플형태로 지정해줄 수 있다.**
#    --> sorted( data, ken=lambda x: (x[0],x[1]))
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### input() == sys.stdin.readline()
### print() == sys.stdout.write(   + '\n')
######################################################
N = int(input())

data = [ list(map(int, input().split()))  for _ in range(N)]
data = sorted(data, key=lambda x: (x[0], x[1]))
print(data)

# for i in range(1, len(data)):
#     if data[i-1][0] == data[i][0] :
#         if data[i-1][1] > data[i][1]:
#             # 이렇게만하면... 전후만 비교하므로.. 같 같 작 -> 같 작 같 의 상황이 와버린다.
#             # 정렬이란... 전후만 하는게 아니라. 해당 그룹(1번재 원소 같은 전체)와 비교해야한다..
#             # 그래서 삽입정렬(i-1부터 shift ), 선택정렬(i+1~끝까지 swap) 이 있는 듯..

#             data[i][1], data[i-1][1]  = data[i-1][1], data[i][1]

print(data)
for x,y in data:
    print(x, y)  
