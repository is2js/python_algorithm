# 느낀점 : 
#  - 격자를 넘어가는 막대기 -> try except로 넘어가도록 pass


################ Input From input.txt ################
import sys

sys.stdin = open("./input.txt", "rt")
######################################################
# https://codeup.kr/problem.php?id=6097
w, h = map(int, input().split())
n = int(input())

# sticks = [[], []] # 
matrix = [[0]*h for _ in range(w)]

for _ in range(n):
    length, direct, x, y = map(int, input().split())
    if not direct:
        for i in range(y-1, (y-1)+ (length-1) + 1):
            # 격자를 넘어가도 되면, 무시하도록 처리해줘야한다.
            try: 
                matrix[x-1][i] = 1
            except IndexError:
                pass
    else:
        # (3,0) -> 길이3 -> 포함해서 시작이면.. 길이3-1 -> 2를 더한 것(3,0) ~ (3+2,0)까지 진행 -> range라서 +1까지
        for i in range(x-1, (x-1)+ (length-1) + 1):
            # print(i, length, x, y)
            try: 
                matrix[i][y-1] = 1
            except IndexError:
                pass


for row in matrix:
    print(*row)
