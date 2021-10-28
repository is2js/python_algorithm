# https://www.acmicpc.net/problem/2504 괄호의값
# 느낀점:
# - 참고 블로그: zero_woo: https://ywtechit.tistory.com/201
# - 참고 블로그2: 코딩하는 금융인: https://codingspooning.tistory.com/68
# * 내풀이 문제점: 괄호가 올바른지는 먼저 확인 b 함수 -> 그래야,, 본 풀이시 올바른 경우의 괄호가 올 것이라고 기대할 수 있다.
# * 1. 올바른지를 먼저 판단하면 -> if stack and stack[-1] == p_dict[i]을 걱정할필요가 없어진다.
# * -> [항상 맞는 괄호]가 있을테니, [원본의 직전괄호가 뭐냐에 따라 달라지도록 로직만 짜면 된다.]
# * 2. 같은 level들을 한꺼번에 계산할 수 있게, stack에 () 짝매칭된 괄호를 숫자로 변형해서 넣어놓기 logic!!!!!!!!
# * 원본에서 본 직전괄호가.. 여괄이 아니라 닫괄이었다? ->
# * -> [현재 닫괄]가 매칭되는 여괄이 나올때까지 pop후 다 더한다. 
# * -> [내 매칭  여괄]나올때까지를 같은 level로 본다.
# * -> 그럴려면 <직전이 여괄이면, 괄호가 아니라 연산할 숫자로 대체해서 넣어놓자!!>
# * --> 직전여괄을 pop하고 그자리에 계산된 숫자를 집어넣어 () -> 2, [] -> 3으로 변환시킨다.
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################

p_dict =  {')':'(',']':'['}
parentheses = input()

def check_valid(parentheses):
    stack = []
    
    for p in parentheses:
        if p in ['(', '[']:
            stack.append(p)
        else:
            # 닫괄 만날시, stack이 차있고 & top에 잇는 것이 짝맞아서 빼내야함.
            if stack and stack[-1] == p_dict[p]:
                stack.pop()
            else:
                # stack이 비거나, top에 짝매칭안되면 탈락.
                return False
    
    return False if stack else True


def calc_num(p):
    # (()[[]])([]) -> 이미 올바른 괄호문자열임이 증명된 상태라.
    stack = []
    for i in range(len(p)):
        # 여괄일 땐, 그냥 쌓는 것은 똑같다. pop할 이유가 없어서 맨 위에 배치
        if p[i] in ['(', '[']:
            stack.append(p[i])
        # 닫괄 만날시, 
        else:
            # stack이 차있고 & top에 잇는 것이 짝맞아서 빼내야함. 
            # *-> 이미 올바른 괄호열이라.. 조사할 필요 없다!!!
            # *-> [항상 맞는 괄호]가 있을테니, [ 원본 직전괄호가 뭐냐에 따라 달라지도록 로직만 짜면 된다.]
            # if stack and stack[-1] == p_dict[i]:

            # * 원본에서 본 직전괄호가.. 여괄이 아니라 닫괄이었다? ->
            # * -> [현재 닫괄]가 매칭되는 여괄이 나올때까지 pop후 다 더한다. 
            # * -> [내 매칭  여괄]나올때까지를 같은 level로 본다.
            # * --> 그럴려면 <직전이 여괄이면, 괄호가 아니라 연산할 숫자로 대체해서 넣어놓자!!>
            if p[i-1] in [')',']']:
                # 직전이 닫괄이라면....  현재닫괄은... 바깥쪽이다. -> 안쪽은 미리 숫자로 변형되어있으니
                # -> 바깥쪽 닫괄에 매칭되는 여괄이 나올때까지 pop해서 계산하자.
                # * 이미 다른 경우에서, 닫괄직전이 여괄이라서 숫자로 변형되어 stack에 넣어놓은 상태일 것이다.
                temp = 0
                # while stack[-1] != p_dict[p[i]]:
                print(p_dict[p[i]],stack[-1])
                while stack[-1] != p_dict[p[i]]:
                    # 매칭되는 여괄이 나올때까지, 내부level은 이미 숫자로 변형되어져있을 것임.
                    temp += stack.pop()
                # 여기는.. stack[-1] == 매칭여괄'('인 상태다. 이건 더할 필요없다.
                
                # *매칭되는 여괄까지 빼줘야한다. 빼고 곱해야함.
                stack.pop()


                # * 이제 내부level의 숫자들이 +로 temp에 계산되어져있으니, 닫괄의 숫자로 곱해야함
                # *-> 곱한뒤 숫자로 변경해주자! 다음 연산을 위해서
                stack.append(temp * (3 if p[i]==']' else 2))
            else:
                # * 이제, 닫괄인데 -> 직전게 여괄이면 무조건 숫자로 변환시키고
                # * -> 변환된 숫자를 stack에 넣어놓아야, 해당 level 전체를 pop시켜 연산이 가능해진다.
                val = 2 if p[i]==')' else 3
                stack.pop() # 여는 괄호를 뺀다.
                stack.append(val) # 그자리에 계산된 숫자를 집어넣어 () -> 2, [] -> 3으로 변환시킨다.
    # 올바른 것만 들어올테니 이런 것도 검사할 필요가 없다.
    # return False if stack else True

    # 다돌았으면, stack에 계산된 값을 반환해준다.
    # 이 때, 닫괄마다 숫자1개로 주어지는데, () [] 같은 경우는 다 더해줘야한다.
    # stack.pop()
    return sum(stack)


if check_valid(parentheses):
    print(calc_num(parentheses))
else:   
    print(0)




