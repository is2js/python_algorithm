################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### import sys
### input == sys.stdin.readline
######################################################



n, k = map(int, input().split())

from collections import deque

dq = deque(list(range(1, n+1)))
res = []




    


while dq:
    if k-1>0 :
        for _ in range(k-1):
            dq.append(dq.popleft())
    res.append(dq.popleft())
        
if n==1:
    print(f"<{res[0]}>")
else:
    answer = ', '.join(map(str, res))
    answer = "<" + answer + ">"
    print(answer)
        
        
        

            
        
        
        