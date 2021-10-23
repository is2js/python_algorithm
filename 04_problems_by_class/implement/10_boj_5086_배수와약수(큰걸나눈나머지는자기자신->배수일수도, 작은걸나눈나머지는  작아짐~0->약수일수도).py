# 느낀점: 
# a % b 에서 b자리에 더 큰수가 있다면 a가 그대로 나온다.
# 
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



while True:
    a, b= map(int, input().split())
    if a ==0 and b==0:
        break
    
    elif b % a == 0:
        print("factor")
        
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")
        





