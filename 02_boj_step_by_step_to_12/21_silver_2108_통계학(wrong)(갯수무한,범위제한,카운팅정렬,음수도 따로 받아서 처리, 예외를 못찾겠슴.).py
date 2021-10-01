# 느낀점 :  input의 갯수가 너무 많으면서, 범위는 한정적 + 중복될 때 -> index라 치고 +1 카운팅하는 카운팅정렬
# 갯수가 list에 담을 수 없을만큼 많다 -> 직접 안받음 -> 범위가 한정적이다 -> 그 범위를 index로 하는데, 받았다 치고 갯수만 카운팅한다.
# 카운팅 정렬은 대응되는 수 - index가 양수만 가능인데.. 음수는 따로 배열을 하나 더 만든다.
# 일단, 50만개까지 N이 들어오는데 다른풀이에서는 sys.stdin.readline + append로 받아졌다고 함.
# - 반례를 못찾겠슴.. -> 질문해서 찾음. 중앙값 정렬이 안됬음. 음수를 양수*-1로 만들 땐, 그 정렬순서가 뒤바껴버린다.(오름차순 -> 내림차순).. 합치기전에 다시 정렬해줘야하는 번거러움이 있었음.
# -> 음수를 새로운 배열의 index로 받지말고, -4000 0 4000을 .. k+4000 = index로 두고.. 한원시 -4000해서 쓰면 될듯하다.
# -> 반올림을 일반적으로 하려면, 함수를 만들자. k - math.내림(k)(기준, 정수이자 상수) 차이가 0.5아래면.. 그냥 내림 / 내림정수에서 0.5이상이면 올려.
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### input() == sys.stdin.readline()
### print() == sys.stdout.write(   + '\n')
######################################################
import sys
N = int(sys.stdin.readline())

positive_counting = [0]*4001
negative_counting = [0]*4001

for _ in range(N):
    k = int(sys.stdin.readline())
    if k >= 0:
        positive_counting[k] += 1
    else:
        negative_counting[abs(k)] +=1

negative_list = [[-idx]*val for idx,val in enumerate(negative_counting) if val >0 ]
 # negative_list는  양수오름차순 * -1이라서..  -1, -2, ... 등의 내림차순으로 정렬됨..ㅠㅠ
negative_list.sort()
positive_list = [[idx]*val for idx,val in enumerate(positive_counting) if val >0 ]
total_list = negative_list + positive_list

# 2차원 리스트를 1차원까지 가서 각각을 이어붙이기
from itertools import chain
total_list =  list(chain(*total_list))



import math
def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)
print(normal_round(sum(total_list)/len(total_list)))

print(total_list[(len(total_list)//2)])


from collections import Counter
count_dict = Counter(total_list)
max_value = max(count_dict.values())
max_list = [ key for key, value in count_dict.items() if value == max_value]
if len(max_list)==1:
    print(max_list[0])
else:
    #print("최빈값", sorted(max_list))
    print(sorted(max_list)[1])

print(max(total_list) - min(total_list))



