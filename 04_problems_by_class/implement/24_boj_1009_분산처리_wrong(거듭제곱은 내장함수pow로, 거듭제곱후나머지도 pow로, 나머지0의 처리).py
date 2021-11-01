# 느낀점:
# * 1. 10개 단위라, %10을 사용했다면, 1부터 시작하는, 나머지0이 아닌 -> 10번째 컴퓨터를 표기할 방법을 따로 처리줘야한다.
# * 2. x**y : 시복N --> 무조건 시복 O(1)의 내장함수 pow(x,y)를 쓰자(재귀?)
# * -> pow(base, exp, mod)는 3번째 인자로 매 연산마다 <내부처리>를 통해 <나눈 나머지를 빠르게 구할 수 있다>
# --> 제곱은 pow(a, b), 제곱 & k로 나눈 나머지라면 pow(a, b, k) 
# * 3. if not (i%k)의 활용
# * 3-1) 나머지0으로 배수판단 -> 1부터 들어오도록 하는 전제가 필요함.
# * 3-2) 나머지0으로, mod 0을 n으로 처리해주기
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################
import sys 
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    # pow(base, -exp, mod)
    mod = pow(a,b, 10)
    if not mod:
        mod += 10
    print(mod)
            
    
    
# import timeit
 
# def show_timeit(command, setup):
#     print(setup + '; ' + command + ':')
#     print(timeit.timeit(command, setup))
#     print()
 
# # Comparing small integers
# show_timeit('a ** b', 'a = 3; b = 4')
# show_timeit('pow(a, b)', 'a = 3; b = 4')
# show_timeit('math.pow(a, b)', 'import math; a = 3; b = 4')
 
# # Compare large integers to demonstrate non-constant complexity
# show_timeit('a ** b', 'a = 3; b = 400')
# show_timeit('pow(a, b)', 'a = 3; b = 400')
# show_timeit('math.pow(a, b)', 'import math; a = 3; b = 400')
 
# # Compare floating point to demonstrate O(1) throughout
# show_timeit('a ** b', 'a = 3.; b = 400.')
# show_timeit('pow(a, b)', 'a = 3.; b = 400.')
# show_timeit('math.pow(a, b)', 'import math; a = 3.; b = 400.')