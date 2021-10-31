# 느낀점:
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
arr = arr[1:n+1]
for i in range(len(arr)):
    k = i%20
    if k == 19:
        print(arr[i], end="\n")
    elif i == len(arr) - 1:
        print(arr[i], end="")
    else: print(arr[i], end=" ")


