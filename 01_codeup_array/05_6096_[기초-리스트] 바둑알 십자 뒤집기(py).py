# 느낀점
# 0, 1 은 bool()로 T/F를 넘나들며, T/F에서만 not으로 서로가 F/T로 쉽게 바뀐다.
# - 바뀌었으면 다시 int()로 넘어온다.
################ Input From input.txt ################
import sys

sys.stdin = open("./input.txt", "rt")
######################################################
# N = int(input())
# print(N)

data = [ list(map(int, input().split())) for _ in range(19)]


N = int(input())
for _ in range(N):
    x, y = list(map(int, input().split()))
    # print(x, y)
    # x-1번째 index행 뒤집기 / col은 전체돔.
    for col in range(19):
        data[x-1][col] = int(not bool(data[x-1][col]))
    
    for row in range(19):
        data[row][y-1] = int(not bool(data[row][y-1]))


for row in data:
    print(*row)



# https://codeup.kr/problem.php?id=6096
