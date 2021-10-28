# 느낀점:
# * 1. 16진수, 8진수를 1자리마다 접근하면 이미 십진수표기가 되었으나, isalpha()벳인경우만 변환시키면 된다.
# * 2. 진수변환은 일단 [n->10진수]로 일단 나타낸다음, [나중에, 한번에.. 10진수->n진수]를
#  - 1) 비트연산(내부2진수 자동변환후, n-1, .. 1,0 번재 index조회로 있을 시, '1' 없을시 '0'으로 채우기)
#  - 2) 나눌수 있는만큼 나눠서 나머지를 거꾸로 읽기
#  - 3) python format( ,'b') or '#b' or 'o' or '#o' or 'x' or '#'x로 변환하면 된다.
# 3. n진수->10진수는 string -> int(, base=n)로 돌아온다.
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
######################################################

import string
hexa_to_decimal = { key:value for key, value in zip(list(string.ascii_uppercase[:7]), range(10, 17))}

T = int(input())

for i in range(T):
    N, hexa = input().split()

    res = ''# 2-4)

    for x in hexa:
        # 1. 16진수 1자리는 기본적으로 10진수표기9까지 + 알파벳이니
        # - 16진수는 알파벳만 처리하면 10진수로 변환가능하다.
        if x.isalpha():
            x = hexa_to_decimal[x]
        else:
            x = int(x)
        
        # 2. 10진수 -> 2진수 변환을.. 비트연산으로 해보자.
        # 2-1) 전제: 10진수를 2진수로 변환안시켜도 [비트연산시 알아서 2진수로 계산]된다
        # 2-2) 틀속1로 bitmask n번째 index 조회: bitmask & (1 << n)를 이용해서 0~n번재 index를 다 조회한다.
        #      16진수 1개는 2진수 4자리를 채우므로, 0123 -> 0부터 3까지 n을 대입해서 조회해서 변환한다.

        #  cf) 2진수 n자리 -> index는 n-1부터 0까지 차지.
        #    --> 16진수 1개당 2진수 4자리 고정 차지 -> 0~3까지
        #    --> 8진수 1개당 2진수 3자리 고정 차지 -> 0~2까지
        
        for j in range(3, -1, -1): # 3, 2, 1, 0
            # 2-3) 비트연산으로 조회=2진수자동변환시 해당자리에 1이 차있다? 
            #     -> 빈 문자열에 해당자리 1로 채우기 
            #     -> 비트연산 & 연산으로 조회했는데 0? == 없다? 0으로 채우기
            if x & (1 << j):
                res += '1'
            else:
                res += '0'

    # print(res)
    print(f"#{i+1}",res)




        








# ========================내풀이
# for i in range(T):
#     N, base_16 = input().split()

#     res = ''
#     for x in base_16:
#         # 16진수 -> 2진수
#         # 16-> 10 ->2 
#         # 1. 16 to 10
#         sixteen_to_ten = map_dict[x] if x.isalpha() else int(x)
#         ten_to_two = format(sixteen_to_ten, 'b').rjust(4, '0')
#         #print(ten_to_two)
#         res += ten_to_two

#     print(f"#{i+1} {res}")