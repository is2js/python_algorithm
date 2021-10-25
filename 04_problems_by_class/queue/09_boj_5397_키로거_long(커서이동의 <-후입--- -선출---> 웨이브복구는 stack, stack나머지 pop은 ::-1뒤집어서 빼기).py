# 느낀점: 
# * 1. 커서이동(or 뒤로가기)으로 인한,  <--pop-- 순으로, 먼저pop 복귀는, --복구--> 순서는 stack의 후입선출을 써야한다.
# * <---a후입b--- 으로 뒤에서부터 빼놨다가(pop),  다시 복구를  ---a선출b---> 형태로 그대로 할거면, stack의 후입선출이다.
# * my) 뒤에서부터 빼놓고, 순서유지 복구 시키려면, stack이다.
#  -> stack(직전과 비교) or stack(커서이동으로 뺏따가 복구) vs queue(넣은순서대로 빼기)
#  - 넣은순서가.. 뒤에서부터 넣기 때문에.. queue는 아니다.
# * 2. 인덱싱안하는 stack은  list대신 -> deque의 append, pop으로 대신써도된다.
#  - queue는 deque의 append, popleft()를 쓴다.
# * 3. 스택을 빼기만 할거면, while pop 대신  [::-1] 뒤집으면 pop한 후입선출효과
#  - 뒤에서부터 1개씩 뺀다?  뒤집어서 앞에서부터 1개씩 뺀다.

# 참고) 스택 사용사례
# 스택(Stack)의 사용 사례
# 1. 재귀 알고리즘을 사용하는 경우 스택이 유용 : 재귀적으로 함수를 호출해야 하는 경우에 임시 데이터를 스택에 넣어준다.
#  -> 재귀함수를 빠져 나와 퇴각 검색(backtrack)을 할 때는 스택에 넣어 두었던 임시 데이터를 빼 줘야 한다.
#  -> 또한 스택은 재귀 알고리즘을 반복적 형태(iterative)를 통해서 구현할 수 있게 해준다.
# 2. 웹 브라우저 방문기록 (뒤로가기) -> 후 앞으로 가기
# 3. my) 커서 왼쪽으로 이동 후 -> 다시 커서 오른쪽 이동시 
# 4. 실행 취소 (undo)
# 5. 역순 문자열 만들기
# 6. 수식의 괄호 검사 (연산자 우선순위 표현을 위한 괄호 검사)
# Ex) 올바른 괄호 문자열(VPS, Valid Parenthesis String) 판단하기
# 7. 후위 표기법 계산

################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# 단계별로 푸시는 분: https://developer-ellen.tistory.com/33 # 고민 많이 하시는 분이라 챙겨놓음.
# 지져스 python 해설 블로그: https://peisea0830.tistory.com/category/BOJ # 해설&그림으로 미쳤음.
# bisect를 최초로 사용한 풀이: https://zereight.tistory.com/672 # N과M 1~11 등 실력순으로 푸신 것 같은데 검색기능이 없다.
######################################################
import sys
input = sys.stdin.readline



n = int(input())


# from collections import deque

for _ in range(n):
    data = input().rstrip()
    stack = []
    # temp = deque([])    
    temp = []

    for x in data:
        if x =='<':
            if stack :
                temp.append(stack.pop())
                # 다음꺼 처리하기전<append되기전>에 temp에서 꺼내놓아야한다?
                # 

        elif x== '>':
            if temp:
                stack.append((temp.pop()))
                # 넣은순(queue)대로 다시 돌려놓기
        elif x=='-':
            if stack:
                stack.pop()
        else:
            stack.append(x)

    # stack이라면 무조건, temp에 남은것 처리
    # print(temp)
    # ㅠ_ㅜ 넣으순이 아니라..커서는.. 나중에 넣은게 먼저나와야한다.
    # x b < : x ? [b]
    # x b < < :  ? [b x] 넣은 b 순대로x 나와야하냐? 아니다.. 나중에x 넣은 것b 순으로 꺼내야한다.
    # -> stack을 그대로 슴녀 된다.
    # while temp:
    #     stack.append(temp.pop())
    # * 스택을 빼기만 할거면,
    # ->  while pop 대신  [::-1] 뒤집으면 pop한 후입선출효과가 있다.
    print(''.join(stack+temp[::-1]))
            

