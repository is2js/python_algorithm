# 느낀점:
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
######################################################

K = int(input())

if K == 0:
    import sys;sys.exit()

for _ in range(K):
    stack = []
    data = input()
    for x in data:
        if x == '(':
            stack.append(x)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                # ) 닫괄인에 stack이 비었거나  or  stack[-1]이 여괄안나오면 짝이 안맞는 것.
                #  -- 닫괄앞에 또 닫괄있을수 있지 않느냐? (X) 닫괄은 안들어가고 바로 pop 
                print("NO")
                break
    else:
        # 닫괄마다 다 닫혔는데, stack에 남아있다? 탈락
        if stack:
            print("NO")
        else:
            print("YES")


