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

a = int(input(), base=2)
b = int(input(), base=2)

# ~ 연산은 2의보수로 출력된다.
# -> 반전의 계산을 할게 아니라, 반전출력용은 xor1111111111로 해준다.
# n자리 111111111를 만드는 방법은?
one_mask = 2^(10**6)-1
# 근데.. 0001000에서 앞에 000도 반전시켜벌임.. 0이어야함..

# bin()을 때리면, string이며, 0b를 제외하고, 앞쪽 0은 다 짤린 문자열
# -> len()-1로 가장  첫번째의 인덱스(뒤에서 0부터 시작하니)
# -> index는 필요없고 그len()만큼 1로 채워지면 될듯?


a_len = len(bin(a)[2:])
a_mask = int("1"*100000, base=2)
b_len = len(bin(b)[2:])
b_mask = int("1"*100000, base=2)


print(bin(a&b)[2:].rjust(10000,"0"))
print(bin(a|b)[2:].rjust(100000,"0"))
print(bin(a^b)[2:].rjust(100000,"0"))
print(bin(a^a_mask)[2:].rjust(100000,"0"))
print(bin(b^b_mask)[2:].rjust(100000,"0"))