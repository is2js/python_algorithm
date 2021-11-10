# 느낀점:
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################




def cnt_jrl():
    M, N, K = map(int, input().rstrip().split())
    board = [ [0]*(M) for _ in range(N) ]
    for _ in range(K):
        # 1이 탐색가능, 0이 벽.
        X, Y = map(int, input().split())
        board[Y][X] = 1
    
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    def DFS(x, y):
        board[x][y] = 0

        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0<=xx<N and 0<=yy<M and board[xx][yy] == 1:
                DFS(xx, yy)

    cnt = 0
    for i in range(N):
        for j in range(M):
            # 시작좌표마저 탐색 -> 각 시작좌표마다 cnt 세고, 색칠하며빽불가 탐색 끝내야함.
            # - 여기선 각 원소들 갯수는 셀 필요없으니DFS에서 셀필요는 없다. DFS에서는 색칠만
            if board[i][j] == 1:
                cnt+=1
                DFS(i,j)

    return cnt


ret_cnt = []
for _ in range(int(input())):
    ret_cnt.append(cnt_jrl())

print(*ret_cnt, sep='\n')
