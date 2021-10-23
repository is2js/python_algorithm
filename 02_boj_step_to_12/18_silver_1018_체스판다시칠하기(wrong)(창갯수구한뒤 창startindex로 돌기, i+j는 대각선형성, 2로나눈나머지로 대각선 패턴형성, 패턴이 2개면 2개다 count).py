# 느낀점 : https://velog.io/@minzz/BOJ-1018%EB%B2%88-%EC%B2%B4%EC%8A%A4%ED%8C%90-%EB%8B%A4%EC%8B%9C-%EC%B9%A0%ED%95%98%EA%B8%B0-Python
# 1. 창의 갯수만큼, 각 창의 start_index를 row, col별로 돌아준다.
# 2. 체스판의 패턴배열은 i+j가 | 대각선을 형성하며, 이것들이 값이 다 0,0기준으로 일정하다.
# 3. 정답이 2개일 수 있따면, 각각 카운터해서 한번더 비교해야한다.

################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################
N,M = map(int, input().split())
items = [ list(input()) for _ in range(N) ]
# print(items)
curr_mint_count = 8*8

# 1. 행렬을 옮겨다닐 땐, start index를 돈다. 창의 길이는 정해져있어서, 창의 갯수만큼 start index도 0시작에서 움직일 것이다.
# - 0시작은 다 동일하니, 끝이 어디까지인지 계산한다.
# ** [처음창의 끝 ~ 마지막창의 끝]으로 계산하면 되는데, 그 갯수는 last - first + 1 일것이다 서로 포함하니까**
# ** 끝 계산을 통해, k개의 창이 생긴다 ->  start_index도 0부터 k번 이동한다.**
for start_row_index in range( N-8+1 ):
    for start_col_index in range( M-8+1):
        # 2. 체스판은 0101의 패턴과 동일하다.
        # **패턴배열은 0101로 보고 %2==0 홀짝을 활용한다**
        # **정답이 2가지가 있으며, 그것을 각각 구해서 비교(min)해야함. 나는 1개 밖에 안구함.**
        # - 0,0의 색이 정답이라고 가정하고 채점했다.
        # - 하지만, 0,0의 색이 틀린 색일 수도 있다. 정답은 2가지로 채점해야함.
        # 2-1. 0,0의 정답이 'B'인 경우라고 치고,짝수들은 다 b이어야하는데 !=b일 경우 count+1
        count_b = 0
        count_w = 0
        for row in range(start_row_index, start_row_index+8):
            for col in range(start_col_index, start_col_index+8):
                # **3. 행렬에서 i+j는 | 대각선(좌측아래로 내려가는)으로 동일한 값을 가진다.**
                #      체스에서도 마찬가지 일듯 싶다. 이것들을 2로 나눈 나머지는, 대각선별로 0/1/0/1로 나올 것이다.
                # 00[0] 01[1] 02[2] 03[3]
                # 10[1] 11[2] 12[3] 13[4]
                # 20[2] 21[3] 22[4] 23[5]
                # 30[3] 31[4] 32[5] 33[6]
                # 3-1) 0으로 이루어지는 대각선 -> 0,0과 값이 동일한 대각선이다.
                # b라면, 모두 b를 가져야한다.
                if(row+col)%2 ==0:
                    # B가 아니라면, B어야햐는데.. (가정) -> count_b로 센다.
                    if items[row][col] !='B':
                        count_b+=1
                    if items[row][col] !='W':
                        count_w+=1
                # b라면, 여기는 모두 w를 가져야한다. -> W가 아니라면, count_b에 색칠해야할 것으로 센다.
                else:
                    if items[row][col] !='W':
                        count_b+=1
                    if items[row][col] !='B':
                        count_w+=1

        # 4. 어느것이 정답이든 1개의 창마다 적은 값을 챙긴 뒤, 
        #  모든 창을 돌면서 update한다.
        count = min(count_b,count_w)
        curr_mint_count = min(curr_mint_count, count)


print(curr_mint_count)





# n_case = N-8+1
# m_case = M-8+1

# case_matrix = []
# for n in range(n_case):
#     for m in range(m_case):
#         case_matrix.append(items[n:8+n][m:8+m])

# min_count = float('inf')
# for matrix in case_matrix:

#     curr_count = 0
#     ###
#     color = matrix[0][0]
#     for row in matrix[::2]:
#         curr_count += sum([ odd!=color for odd in row[0::2]])
#         curr_count += sum([ odd==color for odd in row[1::2]])
#     for row in matrix[1::2]:
#         curr_count += sum([ odd==color for odd in row[0::2]])
#         curr_count += sum([ odd!=color for odd in row[1::2]])

#     min_count = min(min_count, curr_count)

# print(min_count)
        
    


