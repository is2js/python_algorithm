# 느낀점:
# * 갯수가 1개이하일 수 있으면 reduce로 누적(곱, 합?)하지말자.
# * 조합을...각 그룹당 1개씩만 뽑아서 할거면, nC1의 곱으로 한다. product는 각 그룹당 모든 조합이다.
# * 각 그룹당 0이 나올 수있는 경우에는, 각 그룹당 0인 경우를 직접 세지말고, 전체다 nC0 + nC1까지 고려한 뒤, 모두0인 1가지 경우만 빼면 된다.
#  ->  (nC0+nC1) * (mC0+nC1) ...   -1

################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################

import math

n_factorial = math.factorial(int(input()))


discover_not_zero_idx = 0
cnt = 0
for idx, x in enumerate(str(n_factorial)[::-1]):
    if x != '0':
        break 
    cnt+=1

print(cnt)

    
