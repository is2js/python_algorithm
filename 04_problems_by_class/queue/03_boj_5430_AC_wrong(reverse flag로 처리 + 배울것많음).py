# 느낀점:
# 1. strip("")은 여러기호 연속해서 적어넣어도, 알아서 하나씩 다 일괄제거해준다.  -> ("[]()") :  괄호 알아서 순서상관없이 다 제거 
# -> "[dd|dd)]".strip("()[]|") --> dd|dd : |기호빼고 다 1개씩 알아서 처리해줌
# --> strip("[]")가 알아서 일괄처리가 아니라  [1:-1] 형태로 내부만 추출해나가버리기도 한다.
# 2. n <= 100,000 -> 최대 O(n log n) 안으로 풀어야함.
# -> 함수 p 가 RDD 로 주어지면, 어찌됐든 R, D, D 식으로 리스트 p를 한 번 탐색은 해야할 터,
# --> 각 for p로 기본 시간복잡도는 O(n) --> 그 내부에서는 O(lg(n))에 끊어야하는데 사실상 O(1)로 끊어라는 뜻이다.
# --> list의 append, pop-O(1) 제외 다 금지 된다.
# ---> index를 땡겨야하는 `insert, del, index, reverse` -> O(n)  + slicing([a:b]) : O(b-a)  + sort, sorted: O(nlgn)
# --> for p를 빠져나와서는 출력직전에 .reverse는 상관없다.
# **3. 'D' 의 경우, 첫 번째 원소를 pop 해야 하므로, deque사용한다!**
# -> popleft() 를 사용함으로써 O(1) 만에 끝낼 수 있다.
# **인덱스 접근은 양 끝에서 O(1), 하지만 중간 데이터에 접근한다면 O(N)으로 느려진다. 빠른 인덱스 접근을 원한다면, 리스트를 사용하라.**
# 4. R마다 실제로 뒤집는게 아니라 <뒤집는다고 치고의 상황> + flag를 걸어놓는다.
# ** 3항연산자로 flag변수 업뎃 방법:flag=False   flag = False <--(1) if flag else (2)--> True
# -> R or D 상황밖에 없으므로 <R 상황에 따른 D만 고려> + <출력시는 R고려 진짜 뒤집어 출력>
# -> 정상인 체, D? -> popleft()
# -> 뒤집혀진 체, D? -> pop()
# -> 뒤집혀진 체, 종료? -> for다 끝나고, < 나와서 reverse후 출력>
# 5. 문자열형태의 빈 리스트 "[]"는 그냥 처리하지말고 =[]로 초기화하는게 빠르다.

# 배열 다만들고, 출력시에는 reverse  = [::-1] 사용은 시간복잡도 기본 O(n) 중 하나로 반영될 것이다.

################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input == sys.stdin.readline
######################################################
from collections import deque
t = int(input())

for _ in range(t):
    p = list(input())
    n = int(input())
    # strip | 체크
    # split 빈문자열''에 -> .split(",")시 빈list[]로 변함 체크
    if n>=1:
        array = list(map(int, input().strip("[]").split(",")))
    else:
        # 빈 list -> str([]) -> stri으로  "" -> split()으로 [""]이 됬다면..
        # -> 빈문자열이 list안에 있으면, 길이를 가지고 + pop가능한 상태가 되어버림
        # -> reverse와 delete는 필요없으니 걍 error로 예외처리로서 continue하고 건너띄워야할듯
        # -> 그래도 input()은 있어야지, 받아놓고 다음ㄱ ㅓㅅ으로 간다.
        # array = input().strip("[]").split(",")
        # my) 빈문자열 list는 그냥 안받고, = [] 로 선언해버리기
        k = input()
        array = []
        # print(array)
        # print("error")
        # continue

    # print(p, n, array)

    dq = deque(array)

    reversed = False

    # for내부에서는 .reverse() 등의 메소드 금지 상황
    for func in p:
        # print(func, reversed)
        # 뒤집혀진 상태인지 체크하는 flag변수
        if func == 'R':
            # my) 삼항연산자를 활용한 flag 업데이트
            # <flag> = False <- [if <flag> else] -> True
            reversed = False if reversed else True
        else:
            if dq:
                if reversed:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                print("error")
                break
        # print(func, reversed)
    else: 
        if reversed:
            dq.reverse()
        print(f"[{','.join(map(str, dq))}]")


    

    # # 내풀이============================================
    
# p_dict = {
#     'R': reverse,
#     'D' : delete,
# }
# # **이 문제의 핵심은 reverse(O(n))를 안쓰고 덱으로 해결하는 것**
# # - append -> O(1), pop-> O(1)
# def reverse(dq):
#     # dq.reverse()
#     if dq:
#         stack =[]
#         while dq:
#             stack.append((dq.pop()))
#         # dq = deque(stack) -> 이게 기존 dq를 덮어쓰진 못한다. local에서 생성한 거라
#         for k in stack:
#             dq.append(k)

#     return True

# def delete(dq, reversed):
#     if dq:
#         if reversed:
#             dq.pop()
#         else:
#             dq.popleft()
#         return True
#     else:
#         return False

    # # 시간을 줄이기 위해, RR이 연속해서 나온 경우는 생략함.
    # # while 'RR' in p:
    #     # p = p.replace('RR','')
    # for func in p:
    #     result = p_dict[func](dq)
    #     #print(dq, result) 
    #     if not result:
    #         print("error")
    #         break
    # else:
    #     print(f"[{','.join(map(str, dq))}]")   





