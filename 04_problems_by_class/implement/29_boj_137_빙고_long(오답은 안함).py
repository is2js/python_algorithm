# 느낀점:
# https://www.acmicpc.nart를 개별로보고 새 배열에 넣는다?
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################


def check_zero(arr):
    row_zero_cnt, col_zero_cnt, diag_zero_cnt = 0, 0, 0
    for i in range(len(arr)):
        # check row
        for ele in arr[i]:
            if ele != 0:
                break
        else:
            row_zero_cnt+=1

        # check column (zip으로 뒤집어서 하는게 더 빠를 것 같긴한데, 칼럼고정 행을 돌면서 0의 갯수를 판단한다.)
        for j in range(len(arr)):
            if arr[j][i] != 0:
                break
        else:
            col_zero_cnt+=1

    for i in range(len(arr)):
        if arr[-(i+1)][i] !=0:
            break
    else:
        diag_zero_cnt+=1

    for i in range(len(arr)):
        if arr[i][i] !=0:
            break
    else:
        diag_zero_cnt+=1


    return row_zero_cnt + col_zero_cnt+diag_zero_cnt, row_zero_cnt, col_zero_cnt

arr = [list(map(int, input().split())) for _ in range(5)]

from itertools import chain
data = list(chain(*[list(map(int, input().split())) for _ in range(5)]))

cnt=0
for x in data:
    cnt+=1

    for row in arr:
        if x in row:
            row[row.index(x)] = 0
            # check function
            # row5, col5, diagonal2개
            result = check_zero(arr)
            if result[0] >= 3:
                print(cnt)
                exit()
            

        

