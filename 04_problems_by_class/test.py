# 느낀점:


################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
######################################################
import sys

n = int(input())

stack = []
i=1
result = ''
for _ in range(n):
    k = int(input())
        
    # 1. 일단, 1~n사이의 숫자가 있으며, k까지는 stack에 집어넣어야한다.
    if not stack :
        stack.append(i)
        result +='+'
        i+=1

    if stack and stack[-1] < k:
        # 추가... k가 더 큰데, 추가할 i가 더 큰 상태라 추가할 수없는 상황(이미 추가해서 pop)
        if i > k :
            result = "NO"
            break

        while stack[-1] != k:
            stack.append(i)
            i+=1
            result +='+'

    elif stack and stack[-1] > k:
        while stack and stack[-1] != k:
            stack.pop()
            result +='-'
    
    # 어떻게든 같아진 상황
    # -> 같아질려다가 pop으로 인해 고갈되어서 더이상 pop못함 -> k못꺼냄.
    if not stack:
        # print("NO")
        result = "NO"
        break
    else:
        # print(stack.pop())
        stack.pop()
        result +='-'
    # print("result :>>", result)

print(result)

# if result == "NO":
#     print(result)
# else:
#     for x in result:
#         print(x)
            






