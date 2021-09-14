################ Input From input.txt ################
import sys

sys.stdin = open("./input.txt", "rt")
######################################################
data = list(map(int, input().strip().split()))
print(data)




# https://codeup.kr/problem.php?id=6092
# 내풀이
#  각 번호별 count를 해야한다. dict에 Counter를 써도 될 듯한데, 
#  판단범위를 index로 준 list로 해결해보자.

array = [0] + ([0]*23) # index is 불린 숫자들(범위)

for k in data:
    array[k] +=1

# print(*array)
# print시.. 없는 범위(0) 도 나오므로, 그것을 제외하고 print
print(*array[1:])
