# 느낀점:
# * 1. BFS준비물 3가지
# *  1) 자식범위 MAX 혹은 방향벡터 2) 좌표별 dist(L) -> ck(board) 3) deque에 시작좌표넣고 -> [자식queue에넣을때하는것처럼] dist넣기->ck하기 for 최단거리 1번만 입력
# * 2. BFS기본로직 3
# *  1) while dq or while True or while not cnt 등 이후 -> 꺼내서 -> if 조건:break 
# *  2) 자체처리
# *  3) 자식탐색 -> index검사 + ck검사 -> queue에 넣고 + dist 기록 + ck체크
# * 3. dist로 최단거리를 추출한다. 만약, 시작좌표부터 카운팅한다면 +1해줘야한다.

################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################


N, M = map(int, input().rstrip().split())
board = [list(map(int, input())) for _ in range(N)]

# 준비1. MAX 혹은 방향벡터
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
# 준비2, 좌표별 ck + dis or ck + L=0
dist = [[0]*M for _ in range(N)]
# 준비3. deque에 시작좌표 넣어놓고, ck하기
from collections import deque
dq = deque([(0,0)])

# * my) BFS-최단거리에서 ck(board)배열은... 가장빠른것 한번만 기록후, 다른 가지에서 들러도 좌표별 최단기록(dist)안되게 하기 위함이다.
dist[0][0]=0 # 시작좌표의 최단거리==레벨은 0으로 시작
board[0][0]=0 # 0이 벽..

# 로직1) while dq -> 꺼낸게 목표좌표? 2) while True  if 목표레벨? break의 확인시 종료
while dq:
    # 로직2) 꺼내서 목표지점 맞냐 맞으면 break
    x, y = dq.popleft() 
    
    # * 추가 좌표카운팅(자체좌표)은..자체처리에서 해주자?!
    if x==N-1 and y==M-1:
        break 
    # 로직3) 다음레벨 좌표꺼내서 검사하고 맞으면queue에넣기
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]

        if 0<=xx<N and 0<=yy<M and board[xx][yy]:
            dq.append((xx,yy))
            # 로직4) 큐에 들어가는 자식들만, [dist기록 -> ck표시]해서, 최단거리만 기록되도록 하기.
            # * my) BFS-최단거리에서 ck배열은... 가장빠른것 한번만 기록후, 다른 가지에서 들러도 기록안되게 하기 위함이다.
            dist[xx][yy]= dist[x][y]+1
            board[xx][yy]=0

# 현재 break지점에서 그때의 최단거리를 print하면될듯? 따로 카운트안해도
# 문제는.. 시작좌표는 레벨0 거리0에서 출발.. cnt랑 동일시하려면 +1해줘야한다.
# * 최단거리 = 시작좌표에서 전진횟수 ---> 시작좌표포함 카운팅하려면 +1
print(dist[x][y] + 1)