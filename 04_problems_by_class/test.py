# 느낀점:
# 0. 10^7이 넘어가므로 O(N)으로는 안풀린다. 
# * 1. 끝자리 0의 갯수 = 소인수분해해서 10의 갯수 = min(2의 갯수, 5의 갯수)
# * - N!에서 5의 갯수 --->  N//5 통과시 cnt+=(몫만큼 팩토리얼에 숨어있다!!!), 그 다음 N으로 업데이트 --> 통과조건: 나눈 몫이 0이 아니어야됨. N//5 == 1로 최소한 1개는 남아있을 때까지.
# * - N!에서 5의 갯수 ---> N에서 N//5로 구한 소수5가 들어갈수있는 갯수?
#  - 10//5 -> 5가 2개까지 들어있따?
#  - 10! = [10]->2 9 8 7 6 [5]->1 4 3 2 1  -> e를 n//2개를 까먹었는데, 그 값또한.. n//e개의 e를 나눈 것 과 같다. n! -> n!/ e(n//e)
#  - 10//2 -> 2가 5개까지 들어있따?
#  - 10! = [10] 9 [8] 7 [6] 5 [4] 3 [2] 1 

# 1부터 26사에는 25의 배수가 한 개, 5의 배수는 5개 있다. 
# 숫자 25는 25의 배수로 한 번, 5의 배수로 한 번 총 두 번 카운팅 된다. 이는 26을 25로 나눴을 때와 5로 나눴을 때의 몫과 같다. 즉 N! 에 대해서 5가 몇번 곱해지는지 구하려면 N을 5의 제곱들(5,25,125...)로 나눈 몫을 전부 더하면 된다. 이를 더 일반화해서 N!에 대해서 k가 몇 번 곱해지는지 구하려면 N을 k의 제곱들로 나눈 몫을 전부 더하면 된다.
# * -> 5로 한번 카운팅, 5를 벗겨먹었다치고 5^2의 갯수 -> 벗겨먹은 뒤의 5의 갯수 
# * -> 

# * - N!에서 5를 [N//5]개만큼 벗겨먹었으면.. (cnt+=N//5)
# * - 다음은 [N//5]자체를 [N]으로 업데이트하여, N//5 !에서 반복한다.
# * 2. 소인수분해상 e의 갯수는 N!에서 구할 수 있다. -> nCm -> 팩토리얼단위로 n! / m! * (n-m)! 로 나눈다.

# * 3. why? 2로 파악하거나 5로 파악하거나 둘중에 한개만.. 해당한다고 한다..
# - 각 숫자마다 min(2, 5)가 아니라 .. 모든 숫자에대해 2 vs 5  둘중에 최소값이란다... why?

################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################


#n!의 5 개수 세는 함수
def five_count(n):
    answer = 0
    while n != 0:
        n = n // 5
        print("남", n)
        answer += n
    return answer



#n!의 2 개수 세는 함수
def two_count(n):
    answer = 0
    while n != 0:
        n = n // 2
        print("남", n)
        answer += n
    return answer


n, m = map(int, input().split())

# if m == 0:
#     print(0)
    
# else:       
#     print(min(two_count(n)-two_count(m)-two_count(n-m), five_count(n)-five_count(m)-five_count(n-m)))

# # n!, m!, n-m! 들의 2의 갯수들, 5의 갯수들을 파악해야됌.
# # - element남아잇을때까지 1개씩 벗겨먹고, 나머지를 새로운 n으로 보고 업데이트
def count_element_in_factorial(n, e):
    if n == 0:
        return 0
    cnt = 0
    i = 1 
    while n//e > 0:
        print("내꺼", n//e)
        cnt+=n//e # * n!에서 e의 갯수는,   n에서 n//e로 센다. 그 몫만큼 e가 인수로 들어가있다.
        # * 만약, 한번 더 셀려고하면.. e가 아닌 e^2으로 업데이트해서, 그 n//(e^2)의 몫으로 갯수가 몇갠지 세야한다. 한번 벗겨먹었기 때문이다.
        i+=1
        e = pow(e, i)
    return cnt 

# # print(count_element_in_factorial(0, 2))
# # print(count_element_in_factorial(0, 5))

# # 
# cnt_2 = count_element_in_factorial(n,2) - (count_element_in_factorial(m,2) + count_element_in_factorial(n-m,2))
# cnt_5 = count_element_in_factorial(n,5) - (count_element_in_factorial(m,5) + count_element_in_factorial(n-m,5))

# print(cnt_2, cnt_5)
# print(min(cnt_2, cnt_5))

# print(five_count(25), count_element_in_factorial(25,5))
# print(five_count(12), count_element_in_factorial(12,5))
# print(two_count(25), count_element_in_factorial(25,2))
print(two_count(12), count_element_in_factorial(12,2))
# [12]->6 11 [10]->5 9 [8]->4 7 [6]->3 5 [4]->2 3 [2]->1  1

import math
print(math.comb(12,2) / pow(2, 9))