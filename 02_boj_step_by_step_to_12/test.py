# 느낀점 :  input의 갯수가 너무 많으면서, 범위는 한정적 + 중복될 때 -> index라 치고 +1 카운팅하는 카운팅정렬
# 갯수가 list에 담을 수 없을만큼 많다 -> 직접 안받음 -> 범위가 한정적이다 -> 그 범위를 index로 하는데, 받았다 치고 갯수만 카운팅한다.
# 카운팅 정렬은 대응되는 수 - index가 양수만 가능인데.. 음수는 따로 배열을 하나 더 만든다.
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### input() == sys.stdin.readline()
### print() == sys.stdout.write(   + '\n')
######################################################
N = int(sys.stdin.readline())

positive_counting = [0]*4001
negative_counting = [0]*4001

for _ in range(N):
    k = int(sys.stdin.readline())
    if k >= 0:
        positive_counting[k] += 1
    else:
        negative_counting[abs(k)] +=1


# print(positive_counting[:10])
# print(negative_counting[:10])


# positive_sum = sum([idx*val for idx, val in enumerate(positive_counting) if val>0])
# positive_len = len([x for x in positive_counting if x>0 ])

# negative_sum = sum([idx*val for idx, val in enumerate(negative_counting) if val>0])
# negative_sum = -1 * negative_sum
# negative_len = len([x for x in negative_counting if x>0 ])




negative_list = [[-idx]*val for idx,val in enumerate(negative_counting) if val >0 ]
positive_list = [[idx]*val for idx,val in enumerate(positive_counting) if val >0 ]
total_list = negative_list + positive_list

# 2차원 리스트를 1차원까지 가서 각각을 이어붙이기
from itertools import chain
total_list =  list(chain(*total_list))


# from decimal import Decimal, ROUND_HALF_UP, localcontext
# # https://blog.winterjung.dev/2020/01/06/floating-point-in-python
# # print("산술평균", round((positive_sum+negative_sum) / (positive_len+negative_len)))
# with localcontext() as ctx:
#     ctx.rounding = ROUND_HALF_UP
#     #print("반올림 0.5", round(Decimal(0.5).to_integral_value()))
#     print("산술평균", round(Decimal(sum(total_list)//len(total_list)).to_integral_value()))

# print("산술평균", int(sum(total_list)//len(total_list) + 0.5))
import math
def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)
print("산술평균", normal_round(sum(total_list)/len(total_list)))

print("중앙값", total_list[(len(total_list)//2)])


from collections import Counter
count_dict = Counter(total_list)
max_value = max(count_dict.values())
max_list = [ key for key, value in count_dict.items() if value == max_value]
if len(max_list)==1:
    print("최빈값", max_list[0])
else:
    #print("최빈값", sorted(max_list))
    print("최빈값", sorted(max_list)[1])

print("범위", max(total_list) - min(total_list))



