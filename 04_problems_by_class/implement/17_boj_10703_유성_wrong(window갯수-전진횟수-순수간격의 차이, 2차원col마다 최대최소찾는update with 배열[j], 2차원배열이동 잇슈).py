# 느낀점:
# * 0. 나는 zip 을 통해 특정열에서의 간격(row)를 zip으로 행으로 뒤집어서 확인했다. + 돌면서 최소값은 업데이트로 찾는 버릇 가질 것.
# * 1 window는 [차이]+[1]시작점도 / 전진 = index[차이]만 / a b 사이간격 =  [차이] + [-1]로 둘다 포함안하고 순수간격만.
# * 2. 2차원배열에서 col마다 최대, 최소찾는 update with 배열[j]
# # 2-1. 1차원배열이라면, for 1개 -> [뽑을 기준 값with 현재항]을 최초로 넣어주면서 [저장장소]와 비교하며 update by     저장장소 = max(i=뽑을 기준값with현재항,  저장장소) 로 쉽다
# #  -  curr_min = max( arr[i], curr_min )
# # 2-2. 2차원 배열이며, <매 [?]마다 여러개의 [min,max or agg]를 뽑아야한다면> ----------> [?]를 index로 하는 2차원 배열을 저장장소로 
# # - 여기선, <매 [칼럼S]마다 여러개의 i를 뽑아야하며>  x는 제일 아래값 ==max(row)  / #는 제일 위 값 == min(row)를 뽑아야한다.
# max_star = [float('-inf')] * S # 0~S-1까지 max_star[j]에다가 각 j마다의  max값이 저장된다.
# min_sand = [float('inf')] * S # 0~S-1까지 min_sand[j]에다가 각 j마다의  max값이 저장된다.
# # cf) 큰 수는 비트연산으로 2^n을 바로 생성할 수 있다
# # 1<<2 # 2^2
# # 1<<8 # 2^8

# #2-3. col마다의 값들을 비교하며, 최대값 or 최소값을 뽑아내야하니 2중 반복문까지 들어가야한다.
# for i in range(R):
#     for j in range(S):
#         # 각 원소가 x인 유성들에 대해서만 업데이트 해주는데 -> 각 j마다 max_start[j]를 저장장소로하여 -> 뽑을값:row값을 넣어주면서 & 최대값 업데이트를 시행해야한다.
#         # - 바깥에서 i를 돌고 있으니, 각 i마다 현재j가 바로 돌진 않겠지만, i=0, j=[0]1,2,3,4, 다 돌도고 다음 i=1 에서 j=[0]일때,   arr[0]에서 비교하게 된다.
#         # - 그냥 j마다 비교하고 싶다면, 행을 돌아가게 해놓고 arr[j] 저장장소에서 경쟁하게 하면 된다.
#         if arr[i][j] == 'x':
#             max_star[j] = max(i, max_star[j])
#         if arr[i][j] == '#':
#             min_sand[j] = min(i, min_sand[j])
# print(max_star)
# print(min_sand)
# *3. 2차원배열의 이동 주의사항
#  - 2차원배열에서, 좌표이동시 원본에 이동시키면 덮어쓰기 잇슈가 발생한다.-> ([위에서부터]아래로 이동하면, [아래에 있떤 원본]이 덮어쓰기 당함.)
# .    .    .
# X -> .    .
# X    X -> .
# .    . -> .
# -> 이동방향의 맨끝에서부터 땡겨오거나 or 새로운 공배열을 만들어서 if로 그릴 것들은 기존대로 모두 그리되, 이동할 것만 +좌표를 이용해서 그린다.
# 3-1. 원본에 그리려면, 할당이 되어야하니, string -immutable을 list로 바꿔놔야함.
# arr = [list(r)for r in arr]
# arr
# 3-1-2. 뒤에서부터 올라오는 방법은, index자체를 거꾸로 시작 or 반복문 내부에서 변형index사용이다.
# for i in range(len(arr2)-1, -1, -1):
# [-i + (n-1)] or [ -(i+1)]
# for i in range(len(arr2)):
#     for j in range(4):
#         # i만 거꾸로 접근하게함..일단은...n-1행 0~n-1열 -> n-2행 0~n-1 순으로 돌면서, 유성을 잡아당긴다.
#         if arr2[-(i+1)][j] == 'x':
#             arr2[-(i+1) +(move)][j]='x' # 당기기
#             arr2[-(i+1)][j]='.' # 원본자리에 default 공기넣기
# arr2
# 3-2. 이제 새로운 배열을 default로 만들어놓고, 거기다가 그리는 방법
# -> default를 제외한 모든 요소를 if로 그리고, 이동할 것들은 +move한상태로 그린다.
# copy_arr = [['.'] * 4 for _ in range(len(arr))]
# for i in range(len(copy_arr)):
#     for j in range(len(copy_arr[0])):
#         if arr[i][j] == '#':
#             copy_arr[i][j] = '#'
#         # 애초에 default판에 그릴 때부터 이동된 위치에 그린다.
#         if arr[i][j] == 'x':
#             copy_arr[i+move][j] = 'x'
            
# copy_arr

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






