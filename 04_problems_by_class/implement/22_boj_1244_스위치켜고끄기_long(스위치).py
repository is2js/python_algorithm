# 느낀점:
# * 1. j번째마다 줄바꿈 ->  모든원소 +공백으로 출력하다가  if not (n%j): print() 줄바꿈 추가출력
# -> 이 때, <나머지를 이용한 배수판단은> 1부터 시작해야함.
# * 2. 열린 게이트의 갯수를 확인하려면 list.count(1) 메소드를 사용해서 counting해도된다.
#  -> k in list 처럼, 다 봐야하니 시복은 n이다.(list는 sort빼고는 다 n)
#  -> 참고) list 시복 정리 : https://hyun-am-coding.tistory.com/entry/Python-list-%EC%97%B0%EC%82%B0%EC%97%90-%EB%94%B0%EB%A5%B8-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################
import sys 
input = sys.stdin.readline

n = int(input())
arr = [0] * (n+2) # arr[1:n+1]
arr[1:n+1] = list(map(int, input().split()))
# print(arr[1:n+1])



def turn(arr, num):
    arr[num] = (arr[num]+1)%2


for _ in range(int(input())):
    sex, switch_num = map(int, input().split())
    #print(sex, switch_num)
    if sex == 1:
        for i in range(switch_num, n+1,switch_num):
            turn(arr, i)

    else:
        # 기본적으로 받은 스위치는 한번 바꾼다.
        turn(arr, switch_num)
        
        left = switch_num-1
        right = switch_num+1
        while left >= 1 and right<=n and arr[left] == arr[right]:
            #if not (arr[left] == arr[right]):
            #    break 
            turn(arr, left)
            turn(arr, right)
            left -=1
            right +=1
            #print(arr[1:n+1])


    # print(arr[1:n+1])
    # break
# my) -> 0번부터 나오게 인덱싱 ->  나머지가 19로서 마지막일때만 줄바꿈. / 전체의 마지막은 "" / 그외에는 중간 한칸 띄우게" "
# arr = arr[1:n+1]
# for i in range(len(arr)):
#     k = i%20
#     if k == 19:
#         print(arr[i], end="\n")
#     elif i == len(arr) - 1:
#         print(arr[i], end="")
#     else: print(arr[i], end=" ")

# * arr를 인덱싱할필요없이 출력자체를  range(len())이 아니라 range(1, len(()))로 쓰면 된다.
# * 일단 다  x" " 형태로 출력하고 + 20의 배수에서만 print() 추가출력
# ** 1부터 나오면 -> 19가 아닌 20의 배수에서 줄바꿈 -> if not (n%target) : 나머지가 False == 0이면 처리
# - my) 나머지0으로 배수판단할시에는 무조건 1부터 시작
# - my) 0이나 False 반환이 참일 경우에는 if not 자체가 참이다.
for i in range(1, len(arr)):
    # 모든 원소 다 우측공백과 출력
    print(arr[i], end = ' ')
    # 20번째일 때 추가출력...
    if not i%20:
        print()





