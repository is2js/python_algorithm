# 느낀점:
# 1. ~은 계산시는 반전계산이나 출력은 2의 보수로 된다. 
# * 2. 반전출력은 ^(xor) 1111111 mask
# - 이 떄, 자리수를 알아야 그만큼 1을 채우며
# - 2^(자리수)-1 을 사용하면 2진수로는 그만큼 1을 채워있다.
# * 3. bin()으로 비트연산결과를 출력시, 문자열이나 0b가 붙어있으므로 떼서 출력한다.
# * 4. mask 등 비트연산할려고 굳이 2진수로 변환할 필요없다. 출력만 bin()[2:]로 하면 될듯.

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

#mask = int("1"*100000, base=2)
mask = 2**100000-1

print(bin(a&b)[2:].rjust(100000,"0"))
print(bin(a|b)[2:].rjust(100000,"0"))
print(bin(a^b)[2:].rjust(100000,"0"))
print(bin(a^mask)[2:].rjust(100000,"0"))
print(bin(b^mask)[2:].rjust(100000,"0"))
