# 느낀점:
# https://www.acmicpc.net/problem/12851
# 0. 할당할라면, 문자열로 받은 숫자를 int로 변환안하더라도 list(input().split()) 한다.
# 1. 좌표탐색에서는, 현재좌표를 재귀함수 dfs(i,j)인자로 준다.
# -> 방향벡터를 준비물로 준비한다.
# 2. 종착역부터 정하며, 값을 return하든 뭐든 한다.
# 3. 종착역 통과시, ck표시 -> 자식 좌표이동 -> index검사 -> (ck표시는 자식X위쪽에서 현재만)  dfs( ii, jj ) -> 종착역 or 그 이상의 값 return되었다고 생각 -> 최종 return  -> 밖에서  dfs(i,j) 사용
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

N = int(input())
A =[ list(input().strip()) for _ in range(N)]

# 1. 격자판도 그래프이며, 4가지 방향만 가져 방향벡터로 저장한다.
# - 동서남북 -> 거리가 1인 애들의 집합
# - dx[0], dy[0]처럼 같은 index로 나와서 세트로 움직인다.
# - 순서대로 +(1,0)의 동 / (0,1) 북 / (-1,0) 서/  (0,-1) 남
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1] # 동북서남


# 3. dfs짜기
# * 특정지점(i,j)를 기준으로 <내부에서 필터링으로 자체위치==1일 경우 +1 반환>의 자체로직 + <추가로 4방향을 살펴볼 건데, 각각 동북서남 방향을 4번을 돌면서 <자체로직이 돌도록 재귀로> >호출한다.
# * (ii,jj)로 표현되는 4방향중에, 그 <그 친구도 1인지를 dfs에 넣기만 하면 자체로직으로서 필터링 되므로> 그 ii,jj에서도 dfs에 넣어 4방향 중 1이 있는지 살펴보겠다 -> 재귀에 넣으면 쭈욱~ 연쇄적으로 다 살펴본다.
# * 이미 체크된 애들은 체크안할 수 있게 <체크배열도 따로 만들어 줄 수 있다>
# -> 각 ~ 마다 index에 대응되서, 체크를 하든, 업데이트를 하든, j에서 경쟁을 하든.... 배열을 만듬

# 3-1. dfs는 주로 현재 위치를 인자로 받는다.
def dfs(i, j):
    # 3-2. dfs는 재귀를 통한 stack으로서 base case(종착역)를 미리 지정한다. 
    # * 이순간부터 빽한다.
    # -> 0을 만나면 <직전stack속 함수에게> 0을 반환한다.
    if A[i][j] == '0': return 0

    # * 4. if return에 안걸렸다 -> <자동 else부분이 되는 것을 생각>
    # A[i][j]가 0이 아니라면? -> 1인 상태다.
    # 1을 0표시해준다? (check해줌. 다시 돌아왔을 때. 갯수 안세도록?)
    A[i][j] = '0'

    ret = 1 # -> 1일 때, 0을 넣어서 ck해주고 갯수+1해준다? 다음 돌아올 땐 <자체1필터링로직에 안걸리게>
    # 5. 현재위치에서 격자판 4방향을 dfs로 탐색할때는 dx, dy를 index수 만큼 4번 반복문을 돌려 처리한다. 
    for way in range(4):
        # 5-1. 탐색할 좌표 먼저 따로 추출
        ii, jj = i+dx[way], j+dy[way]
        # 5-2. 탐색할 좌표가 격자판 내에 있어야함.
        # -> 격자판 내에 없는 탐색좌표는 건너뛰도록 필터링 한 것이다.
        # -> if not () : continue로 바꾸는게 더 좋을듯?
        # if ii<0 or jj<0 or ii == N or jj == N: continue 
        if not (0<=ii<=N-1 and 0<=jj<=N-1 ):continue
        
        # 5-3. 
        # [함수]의 if return 과 마찬가지로 [반복문] if continue를 건너띄었다면, 
        # 그 때서야 본 로직이 나온다.
        ret += dfs(ii, jj) # 바뀐 위치로 4번의 dfs를 호출해서, 정보를 ret에 담는다?
    
    return ret




#7. 각 원소마다 재귀를 돌고 나온 것을 받아준다.
lst = []

# 2. 2중반복문 -> 모든 원소하나 하나를 접근해서, 색칠되어있으면, dfs로 탐색한다.
# -> dfs는 (i, j)로 격자판의 index(내 위치)를 받아서 돌아간다.
for i in range(N):
    for j in range(N):
        if A[i][j] == '1':
            # 6. dfs를 돌고오면, i,j부터 -> 4방향마다 -> 또 그것의 4방향마다 0나오면 멈춰서 다시 직전거로..재귀.. 1의 갯수를 반환한다.(체크로직때문에 원본배열은 0으로 차있을 것임.)
            # print((i, j))
            # print((dfs(i, j)))
            lst.append(dfs(i, j))

print(len(lst))
print('\n'.join(map(str, sorted(lst))))