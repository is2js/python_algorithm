# 느낀점:
# *1. 골드 진입문제. 종착역없이 그래프 [색칠하며빽불가] 1경로 우선 탐색. 자식조건에서 걸리게 됨.
# -> 경로 찾는 우선순위는 DFS특성에 맞게. 제일 먼저 찾는 자식, 기준으로 끝까지 간다.
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################

N = int(input())

g = [[0]*(N+1) for _ in range(N+1)]
ck = [0]*(N+1)

for _ in range(int(input())):
    a, b = map(int, input().rstrip().split())
    g[a][b] = 1
    g[b][a] = 1


ck[1] = 1
cnt = 0

def DFS(v):

    ck[v]=1
    global cnt 
    # 시작좌표를 1번 컴퓨터를 제외하고, 인접한 노드 카운팅
    if v != 1:
        cnt +=1

    for j, val in enumerate(g[v]):
        if val == 1 and ck[j]!=1:
            DFS(j)

DFS(1)
print(cnt)




