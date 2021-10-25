# 느낀점:
# * 1. 배열내, 같은 숫자의 갯수를 Counter가 아닌, < sort + 비교 >로 알 수 있다.
# - 배열내, 같은 문자의 갯수도 정렬해서 비교해가며? 할 수 있을 듯.
# * 2. main함수를 최소화시키고, 반복문 정도만 나열해서 함수를 돌린다.
# * -> 함수내에서 태케를 처리할 때는, 파라미터를 딱히 안받아도 된다?
# * -> 테캐가 아니라 2~3중 반복문을 처리할 때만.. 파라미터를 받는 함수로 정의한다?
# * --> check(i,j,k) 등..
# * 3. 반복문, 조건문, 입력초기화 등으로 코드를 많이 줄일 수 잇다.
# * --> main에서 돌릴 함수 -> 함수내 if return이 나왔으면 -> else는 물론이거나와 < elif >도 할 필요도 없다!
# * 4. main함수에서, 태케마다 기능분리함수->return값을 돌려서 모으는 경우에는, comp로 최대값, 최소값을 바로 써버릴 수 잇도 있음.
# - print(max(  money() for _ in range(int(input()) )))
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
######################################################

# 2. 메인함수에서 각 테케마다 처리될 함수
def money():
    #lst = list(map(int, input().split()))
    # * 3. 배열내, 같은 수 or 문자의 갯수를 찾으려면, sort부터 한다!!
    lst = sorted(list(map(int, input().split())))
    # 4. set()을 이용해서 유니크한 것의 갯수를 확인한다면, 같은 수가 몇개인지 알 수 있다.
    if len(set(lst)) == 1: 
        return lst[0] * 5000 + 50000
    # * 5. 함수안에서 if return은, 걸렸음녀 끝난 상황이므로 딱히 elif처리를 할 필요가 없다.
    if len(set(lst)) == 2: 
        # 6. 2개만 존재한다면, 1-3/3-1 이거나 2-2 이다.
        # * 1-3 이든 3-1이든 sort된 상태이므로, [1]번째요소와 [2]번째 요소는 무조건 같다.
        if lst[1] ==lst[2]:  return lst[1] * 1000 + 10000
        # * else같아도!! 하지말자. return나왔으면!
        # else가 없어도, 2-2상황임. 지금은.  가운데 2개는 무조건 다름. 0,3도 다름.
        return 2000 + (lst[1] + lst[2])*500
    # * 7. 2-a-b 상황이라면, <정렬상태이므로> 연속된 2개가 같은 경우를 찾아야한다.
    # * - 22ab a22b ab22 3가지 경우중에 하나이므로, 그냥 for문으로 다돌려서, [i] == [i+1]걸리면, 딱 1경우밖에 없으므로 return시킨다.
    for i in range(3):
        if lst[i] == lst[i+1]: return lst[i]*100 + 1000
    # * 8. 다 앞에서 return나왔으므로, else나 elif가 없어도, 맨 마지막 경우다.
    # * 맨 마지막 경우: 4개다 다른 경우. -> sorte된 상태므로, 맨 마지막 원소가 젤 크다.
    return lst[-1]* 100


# # 1. main함수는 최소화시키고, 함수안에서 테케 처리하기
# # 10. max값 모으기
# max_money = float('-inf')
# for _ in range(int(input())):
#     # 9. 계산 값이 튀어나올 것이다. 그중에 젤 큰값을 뽑음 됨.
#     max_money = max(money(), max_money)
# print(max_money)

# * 11. 데이터 변형없이 반복되는 값들 중 맥스값만 찾는 거면, max(  ) 함수내부에서 comp를 돌리면 된다.
# -> 함수로 기능분리한 뒤, return되는 값을 모아서 그중 단순 최대값만 원한다면 
print(max(  money() for _ in range(int(input()) )))




# ==================================== 내 코드==============
# from collections import Counter

# max_money = float('-inf')
# # 같은 눈이 4개가 나오면 50,000원+(같은 눈)×5,000원의 상금을 받게 된다. 
# # 같은 눈이 3개만 나오면 10,000원+(3개가 나온 눈)×1,000원의 상금을 받게 된다. 
# # 같은 눈이 2개씩 두 쌍이 나오는 경우에는 2,000원+(2개가 나온 눈)×500원+(또 다른 2개가 나온 눈)×500원의 상금을 받게 된다.
# # 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
# # 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  

# def calc_money(data):
#     max_cnt = max(data.values())
#     val_lst = [ x[0] for x in data.items() if x[1]==max_cnt]
    
#     if max_cnt == 4:
#         return 50000 + (val_lst[0]*5000)
#     elif max_cnt == 3:
#         # val_lst = [ x[0] for x in data.items() if x[1]==max_cnt]
#         return 10000 + (val_lst[0]*1000)
#     elif max_cnt == 2:
#         # val_lst = [ x[0] for x in data.items() if x[1]==max_cnt]
#         if len(val_lst) == 2:
#             return 2000+(val_lst[0]*500) + (val_lst[1]*500) 
#         else:
#             return 1000 + (val_lst[0]*100)
#     else:
#         return max(data.keys())*100



# for _ in range(N):
#     data = list(map(int, input().split()))
#     data = Counter(data)

#     money = calc_money(data)

#     max_money = max(max_money, money)

# print(max_money)
