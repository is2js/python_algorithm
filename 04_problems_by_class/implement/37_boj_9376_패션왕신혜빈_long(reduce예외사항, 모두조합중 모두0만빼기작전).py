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
import sys 
from collections import defaultdict
# from functools import reduce

for _ in range(int(input())):
    map = defaultdict(int)
    n = int(input())
    # reduce 예외처리 2.. 인자가 0개인 경우는 에러가남 (1개인 경우는 작동안함)
    if n==0:
        print(0)
        continue
    for _ in range(n):
        item, category = input().split()
        #map[category].append(item)
        map[category] +=1

    # 각 카테고리마다 택1? (X)
    # print(map.values())
    # print(list(product(*map.values())))
    # break

    # nCk로 풀면.. 복잡하다. nC1   x ( mC1 )  + [둘중에 한쪽만 0이 가능함..]
    # 곱하는 순간 순열이라서.. 우리는 조합을 원함. 그리고 한쪽만 0이 가능해서.. 
    # 전체 - 모두0으로 풀어야한다...
    # (nC0+nC1) * ( mC0+mC1) - 모두0인 1
    
    cummul = 1
    for key, cnt in map.items():
        cummul*=(cnt+1)

    print(cummul-1)



    #print(numbers)
    # 뭐야...reduce는 인자가 1개(카테고리가 1개)인경우 작동을 안하네.. 예외처리해줘야하네
    # if len(numbers)==1:
    #     print(numbers[0])
    #     continue
    # print(reduce(lambda x, y : (x+1)*(y+1), numbers) - 1)
    

    