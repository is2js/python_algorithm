"""
author : ChoJaeSeong
github : https://github.com/is2js
e-mail : tingstyle1
https://rebas.kr/792
title : 테트로미노 공부해보기
description : 
"""

################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### import sys
### input = sys.stdin.readline
######################################################
from collections import deque

N = int(input())

dq = deque(range(1,N+1))

if len(dq)==1:
    print(dq[0])
else:
    while dq:
        
        dq.append(dq.popleft())
        if len(dq)==1:
            print(dq[0])
    
    