# 느낀점:
# 1. 유클리드호제법 원리 -> gcd를 재귀로 구할 수 있다.
# * 원리 : a, b의 최대공약수 == b와 a%b의 최대공약수
#          -> GCD(a, b) = GCD(b, a%b)
#         a%b가 0이 될 경우 해당 b가 최대공약수이다.
# ex) GCD(24, 18) = GCD(18, 6) = GCD(6, 0)
#      마지막에 a%b가 0이 되었기 때문에 24와 18의 GCD는 6이다. 

# 2. lcm = a * b // gcd 로 gcd한번만 나눠주면 된다.
# 2. 최소공배수 (LCM: Least Common Multiple)
# 최소공배수는 유클리드 호제법을 이용해 구한 최대공약수를 이용해 쉽게 구할 수 있다.
# a = x * GCD(a, b) 이고 b = y * GCD(a, b) 이기 때문에 최소공배수는 a*b / GCD(a, b) 이다.
# 해당 수는 a, b 중 어느 수로 나눠도 나누어 떨어지고, 나누어 떨어지는 숫자 중 가장 작은 수이기 때문이다.
#           -> LCM(a, b) = GCD * (a/GCD) * (b/GCD) 
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
######################################################
import sys
#  A & B, A | B, A ^ B, ~A, ~B

a, b = map(int, input().split())

# 1. 유클리드호제법 원리를 이용한 재귀gcd
def gcd(a, b):
    # base case : b자리에는 직전의 a%b가 오며, 이놈이 0인 경우, 그 때의 a(직전의 b)를 출력하면 된다.
    if b == 0:
        return a
    # a와 b의 최대공약수는 -> 횟수가 결국 주는 부분문제 < b와 a를 b로 나눈나머지  의 최대공약수>로 구할 수 있다. 
    # - 대신 a%b가 0일 경우 그 때의 b가 gcd이다.
    return gcd(b, a%b)

# 2. lcm = A * B // gcd 
def lcm(a, b):
    return a*b//gcd(a,b)

print(gcd(a, b))
print(lcm(a, b))


# ===============내풀이============
# import math

# gcd = math.gcd(a, b)

# # lcm = gcd * (a//gcd) * (b//gcd)
# lcm = a*b//gcd

# print(gcd)
# print(lcm)