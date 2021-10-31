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

for _ in range(int(input())):
    room_num = int(input())
    arr = [0] * (room_num+2) 

    for i in range(1, room_num+1):
        for k in range(i, room_num+1 ,i):
            arr[k] = (arr[k]+1)%2
    print(sum(arr))
            
    
    
