# 느낀점:
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

R, S = map(int, input().split())

lst_2d = [list(input().strip()) for _ in range(R)]
import copy
lst_2d_output =copy.deepcopy(lst_2d)


min_distance = float('inf')

# 유성<-> 별간의 최소값  = 이동할 값 구하기
# * 유성이 빈 경우에는.. 건너뜨기
for col in zip(*lst_2d):
    if 'X' not in col:
        continue
    x_right_index = len(col) - col[::-1].index('X') - 1
    shap_left_index = col.index('#')
    distance = shap_left_index - x_right_index -1
    min_distance = min(min_distance, distance)
    
# 이제 원본 2d의 유성을 만날때마다 거리만큼 내린다. -> +row만큼에 찍어주고, 자신은 공기 처리
for i in range(R):
    for j in range(S):
        # 이걸 또.. 하/우 방식으로 탐색해나가면..
        # 위쪽X가 1칸 내려갈때, 바로 아래 있떤 X랑 겹쳐진다.... [XX.  -> .X. -> ..X ]가되어버림........
        # * 한칸씩 내려주고, 있던자리에 표시를 한다면,, 아래쪽부터 탐색되도록 해야한다.
        i2 = -i + R-1 
        j2 = -j + S-1
        if lst_2d[i2][j2] == 'X':
            lst_2d_output[i2][j2] = '.'
            lst_2d_output[i2+min_distance][j2] ='X'

for row in lst_2d_output:
    print(''.join(row))






