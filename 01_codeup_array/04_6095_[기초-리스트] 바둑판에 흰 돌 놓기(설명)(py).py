################ Input From input.txt ################
import sys

sys.stdin = open("./input.txt", "rt")
######################################################
N = int(input())
# print(N)
# data = list(map(int, input().split()))
# pprint(data)

data =  [ [0] * 19  for _ in range(19) ] 

for _ in range(N):
    row, col = list(map(int, input().split()))
    data[row-1][col-1] = 1

for row in data:
    print(*row)
    



# https://codeup.kr/problem.php?id=6095
