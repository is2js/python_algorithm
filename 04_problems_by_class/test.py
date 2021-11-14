# 느낀점:

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
