# 느낀점:
# * 1. 조합과 순열은 product와 달리 1개배열내에서 뽑힌놈제외하고 추가로 n개 뽑는데, 그 차이는,,
# * [조합]은,, 중복X[1번 뽑히면 자기자신빼고] [오름차순으로 빽 없이(배열 왼쪽에 있는 수는 안뽑음) 뽑아서] [N개씩 그룹뽑기] -> 12 13 /  23점점 그룹수가 줄어듬
# * [순열]은,, 중복X[1번 뽑히면 자기자신빼고] [빽가능(순서로 쳐준다) 왼쪽에 있던 수들도 포함해서(내림차순 부분집합도 쳐준다.) 모든 경우의 부분집합을] [N개씩 그룹뽑기] 12 13 / 21 23/ 31 32
# - 내림차순 부분집합도 쳐준다. 2 1 3 4  /  모든 그룹당 갯수가 똑같다.

################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################


N, M = map(int, input().rstrip().split())

from itertools import combinations, permutations

# 조합은,, 중복X라서 [1번 뽑히면 자기자신빼고] [오름차순으로 빽 없이 뽑아서] [N개씩 그룹뽑기] -> 12 13 /  23점점 그룹수가 줄어듬
# lst = combinations((range(1, N+1)), M)

# 순열은,, 중복X라서 [1번 뽑히면 자기자신빼고] [빽가능 왼쪽에 있던 수들도 포함해서] [N개씩 그룹뽑기] 12 13 / 21 23/ 31 32
lst = permutations((range(1, N+1)), M)
for row in lst:
  print(*row)
