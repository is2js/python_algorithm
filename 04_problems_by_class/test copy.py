# 느낀점:
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################
N, M, V = map(int, input().split())

# * 1. DFS탐색 -> 그래프면, DFS든 BFS든 인접행렬, ck배열 만들어야한다.
g = [ [0]*(N+1) for _ in range(N+1) ]
ck = [0]*(N+1)

for _ in range(M):
    # 양방향인 것 같음.
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1


#print(g)

ck[V] = 1


dfs_arr = []
bfs_arr = []

# 2. DFS 탐색시작
cnt=0
def DFS(v):
    global cnt # DFS도 종착역을 node가 아닌 cnt로 잡을 수 있다.
    global dfs_arr
    if cnt==N :
        return 
    
    # 자체처리로서 호출순으로 출력하고 싶다면, 부분문제 호출전에 입력하고 들어간다.
    #print(v, end=" ")
    dfs_arr.append(v)
    cnt+=1

    
    # * 자식 탐색 추가조건 1)갈수있는지 2) 미방문인지 + @ 여기에 준다.
    # -> 최소 지점인것을 먼저 찾아야하네..
    #min_v = v 
    #for j in range(v+1, N+1):
     #   if g[v][j] and ck[j]==0:
      #      min_v = min(min_v, j)

    # * 자식노드를 1~n까지가 아니라, 애초에 g[v]로서 갈 수 있는 후보지들을 돌게하자.
    # -> 6-15 경로의수 문제 풀이와 달라짐. 
    # * 1)갈수있는 곳인지가 한번에 해결된다.
    #for j in range(1, N+1):
    for j in range(1, N+1): # * 이것자체가 최소부터 들어간다?
        if g[v][j] and not ck[j]: # ==0보나는 not 으로
            ck[j]= 1
            DFS(j)
            ck[j]=0
        # * 경로의수를 구하는게 아니라면, 빽 못하도록, 체크를 풀지 않는다.
        #ck[min_v]= 0


DFS(V)
# print()

# # 3. BFS로 탐색
bfs_ck, dis = [0]*(N+1), [0]*(N+1)

from collections import deque 

bfs_ck[V] = 1
dis[V]= 0
dq = deque([V])

bfs_cnt = 0 

# print(dq[0])

while dq and bfs_cnt<N:
    curr = dq.popleft()
    #print(curr, end=" ") # * BFS는 뽑고나서야 확인하고, 자체처리한다.
    bfs_arr.append(curr)
    bfs_cnt+=1

    for next in sorted( num for num, x in enumerate(g[curr]) if x):
        if not (1<=next<=N):continue
        if bfs_ck[next]:continue

        bfs_ck[next] = 1
        dq.append(next)
        dis[next] = dis[curr]+1
        #print(next, end= " ")
        


# print(dis)
print(' '.join(map(str, dfs_arr)))
print(' '.join(map(str, bfs_arr)))

        

    
