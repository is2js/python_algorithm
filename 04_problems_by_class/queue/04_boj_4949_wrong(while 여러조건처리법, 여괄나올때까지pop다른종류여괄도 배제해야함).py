# 느낀점:
# 1. 닫괄만날시, 여는괄호나올때까지 pop하는 조건이 
#   1-1) while stack(pop전 확인->있어야함) and 
# * 1-2) stack[-1] not in others(담긴것은 여괄만! and 담긴 것이 다른종류의 여는괄호가 아니여야함) and 
#       cf) 차집합을 set(lst1) set(lst2)보다  1개만 set(lst1).difference( list 2)로 set1번만 해도된다.
#   1-3) 원하는조건=(필수검사후)마지막조건= <stack[-1] 여괄나오기직전까지> = < stack[-1] != 여괄(match[x] >or  '(' or '[')로 만날때까지 -> 나오는 순간이 만나는 순간임.
# * 2. while 끝: stack[-1] == 만난순간 (조건3이 끝나고 원하는 상황)일 것 같지만.
#   2-1) if not 1-1조건으로서, 여괄만나기도전에 pop되었거나 OR
#   2-2) elif not 1-2조건으로서, 다른종류여괄만났거나 OR
#   2-3) else 그게 아니라면 1-3)으로서 stack[-1] == 여괄인 순간이다.
#   * while [~할때까지] while [not ~함] 앞에 추가 조건이 붙어있다면, 그 상황일때도 고려해라.
# * my) while 조건1 and 조건2 and [~하기직전까지] 
#  -> while을 빠져나온 순간은   if [not조건1] 이거나 elif [not조건2]를 처리한 뒤에야 -> else:[~한 순간]이 온다.
# * my) 반복문 속 반복문에서는 if:break쓰지마라. 2번째 반복문의 조건으로 걸고-> 빠져나와서 순서대로 if not조건1, elif not 조건2 else순으로 처리해라.
# 3. 여러종류가 있을 때, if x== 일부후, 바로 else:하지마라!
# -> x에 올 수 있는 또다른 종류가 남아있다면, if x== elif x== 로 잡아서 처리하기


################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
######################################################
import sys

# 문자열 hash는 case with문을 대신한다. if elif를 대신한다.
match = {
    ')' : '(',
    ']' : '[',
}

while True:
    K = input()
    if K == ".":
        break
    break_flag = False
    stack = []
    for x in K:
        if x in ['(', '[']:
            stack.append(x)
        # 쳌) 영어랑 공백도 올 수 있어서, else가 아닌 elif로 수정
        elif x in [')', ']']:
            # my) 짝원소의 종류가 2개 이상 있는 경우, 다 pop시키면 [(]) 는.. 닫괄로 pop시작시 (를 제거해버린다.
            # * 해당닫괄시-> 해당여괄 나올때까지 & < 다른닫괄이 중간에 나와면 탈락 >
            others = set(match.values()).difference(match[x])
            # print("other :>>", other)
            while stack and stack[-1] not in others and stack[-1] != match[x]:
                stack.pop()

            if not stack:
                print('no')
                #break_flag = True
                break
            
            # * 쳌) 탈락0: 여괄만날때까지 pop하는 도중, <다른종류의 여괄>이 먼저나온다면, 순서가 잘못된 것이다.
            # * 다른 종류 여괄을 어캐 뽑아내지? -> 차집합
            # -> 탈락0보다 뒤에와서 elif로 가야한다. 일단 [-1]로 뽑을 수가있어야한다.
            elif stack[-1] in others:
                print("no")
                # * 여기는 2중 for else썼는데도 내부라서.. flag를 써야한다.
                #break_flag = True
                break
            
            # **만난순간. 여는 괄호도 pop시켜서 짝을 통째로 제거한다.**
            # -> 탈락0, 1이 아닌 순간
            else:
                stack.pop() 
        
    # print(stack)
    # 탈락2: x를 다돌면서 stack을 닫는괄호를 다 제거했찌만, stack에 여는괄호가 남아있는 경우 탈락
    # if not break_flag:
    else:
        if stack:
            print("no")
        else:
            print("yes")
