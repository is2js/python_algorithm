# 느낀점:
# https://www.acmicpc.net/source/34528127

# https://www.acmicpc.net/source/34445222
# : 짤랐으면, 남남이라.. 4part를 개별로보고 새 배열에 넣는다?
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################



def op1(arr):
    return arr[::-1]
def op2(arr):
    return [ row[::-1] for row in arr]
def op3(arr):
    return list(map(zip(*(arr[::-1]))))
def op4(arr):
    return list(zip(*arr))[::-1]

def op5(arr):
    st_points = [(0,0), (0,M//2), (N//2,0), (N//2,M//2)]

    tmp_lst = [ [False]*M for _ in range(N)]

    for (dx, dy) in st_points:
        for i in range(N//2):
            for j in range(M//2):
                if (dx, dy) == (0, 0):
                    mx, my = dx+i, dy+j+M//2
                elif (dx, dy) == (0, M//2):
                    mx, my = dx+i+N//2, dy+j
                elif (dx, dy) == (N//2, 0):
                    mx, my = dx+i-N//2, dy+j
                else:
                    mx, my = dx+i, dy+j-M//2
                tmp_lst[mx][my] = arr[dx+i][dy+j]
    return tmp_lst


def op6(arr):
    st_points = [(0,0), (N//2,0), (N//2,M//2), (0,M//2)]

    tmp_lst = [ [False]*M for _ in range(N)]

    for (dx, dy) in st_points:
        for i in range(N//2):
            for j in range(M//2):
                if (dx, dy) == (0, 0):
                    mx, my = dx+i +N//2, dy+j
                elif (dx, dy) == (N//2, 0):
                    mx, my = dx+i, dy+j+M//2
                elif (dx, dy) == (0, M//2):
                    mx, my = dx+i, dy+j-M//2
                else:
                    mx, my = dx+i -N//2, dy+j
                tmp_lst[mx][my] = arr[dx+i][dy+j]
    return tmp_lst


func_dict = {
    1:op1,
    2:op2,
    3:op3,
    4:op4,
    5:op5,
    6:op6,
}

N, M, R =  map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
R_lst = list(map(int, input().split()))
print(R_lst)
# for r in R_lst:
#     A = func_dict[r](A)

for row in A:
    print(*row)