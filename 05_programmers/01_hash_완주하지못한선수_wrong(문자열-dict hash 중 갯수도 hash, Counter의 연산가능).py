# 느낀점:
# * 이미 범위가 정해진 숫자 -> index에 hash해서 [count]할 수 있다.
#  -> 이범정 숫자 -> 01의 2진수(카운팅은 안됨)에 hash해서 [불켜고/끄고] 할 수도 있지만
#  -> 이범정 숫자 -> 0부터 n쓸려고 n까까지의 배열에 hash해서 [불켜고/끄고] + [count] 할 수도 있지만
# * 이범정 문자열 -> dict에 hash해서 [바로 호출가능]하다.
# * 1. 이범정 문자열 [count] + [빼는 감산까지도] -> dict에 hash시킬 수 있으며
#  -> 동명이인도 +2로 셀 수 있고, 완주자에 있으면 1만 차감시킬 수 있다.
# *  + 문자열의 갯수 hash(dict)는 <더하고 빼기가 가능>해서, 안빼진 나머지를 구할 수 있다.
# * 2. 원래 배열속 갯수는 정렬해서 비교한ㄷ?
# * 3. Counter객체는 dict에 [갯수]를 hash함과 동시에 * [count숫자별 +- & | 연산이 가능하다.]
# -> 대박!
# 4. hash에서 넣고, 꺼내는 것은 O(1) 수식급으로 빠르다.
# * my) 배열내 갯수가 2개 이상의 숫자를 셀 경우, hash해서 counting + 감산까지 -> 더하고 빼자.
# * 5. (중복허용이라도)비슷한 배열과 배열(1개빠진 배열)비교는 <정렬후 zip or 정렬후 index동시접근>으로 달라지는 순간 그놈을 꺼내면 된다.
# * cf) 배열내 중복의 갯수는 -> 배열정렬후, i와 i+1번째를 비교해서 달라지는 순간의 i+1를 추출하면 된다?



# =========== default dict에다가 문자열의 갯수를 hash해서 대응시킴 =========
# -> 동명이인도 +2로 늘어나서 , 차감시 1개만 줄어듬.
from collections import defaultdict

def solution(participant, completion):

    cnt_dict = defaultdict(int)

    for p in participant:
        cnt_dict[p] += 1
    for c in completion:
        cnt_dict[c] -= 1

    return [val for val, cnt in cnt_dict.items() if cnt > 0][0]




# =========  Counter의 연산을 이용한 방법=============
from collections import Counter   

def solution(participant, completion):
    p_cnt = Counter(participant)
    c_cnt = Counter(completion)
    return list((p_cnt - c_cnt).keys())[0]



# ==== hash ( O(1))보다는 비효율적이지만, <정렬 sort (O(NlgN)) >을 이용한 배열내중복 확인(ex>주사위네개) or 배열차이비교(현재 문제) =====
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if not p == c:
            return p
    else:
        # 현재까지 다 똑같다. 1개 더 많은 p에서 맨 마지막 것을 뽑으면.. 다른 1개가 나옴.
        return participant[-1]
        




# ==========================================통과 못한 내 코드
# from collections import Counter

# def check_twins(participant):
#     cnt_dict = Counter(participant)
#     val_lst = [ val for val, cnt in  cnt_dict.items()  if cnt>1]
#     return val_lst[0] if len(val_lst) > 0 else False
    
    

# def solution(participant, completion):
#     no_pass = list(set(participant).difference(completion))
#     if (not check_twins(participant)) or (check_twins(participant) and check_twins(completion)):
#         # 중복이=================
#         # 참여자X - 완료자X  or  중복되었지만 둘다 존재하면..= 둘다통과하면
#         # 중복 고려안해도됨. ->  평범하게 차집합에서 찾으면 된다.
#         return no_pass[0]
    
#     # 문제는.. 동명이인이 3명이상인경우..
    
    
#     # 참여자X - 완료자O ? 있을 수 없음.
#     # 참여자O -> 완료자X -> 그놈만 통과 못한 거... -> 그놈을 출력한다.
#     return check_twins(participant)