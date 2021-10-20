################ Input From input.txt ################
import sys

sys.stdin = open("./input.txt", "rt")
######################################################
N = int(input())
# print(N)
data = list(map(int, input().split()))
# print(data)
print(min(data))




# https://codeup.kr/problem.php?id=6094
# 내풀이

# array = [0] + ([0]*N) # index is 불린 숫자들(범위)

# for k in data:
#     array[k] +=1

# print(*array[1:][::-1])
