# 느낀점:
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################

import sys
input=sys.stdin.readline

N = int(input())


numbers = input().split()
# print(numbers)


    
# print(''.join(numbers))
# print(numbers)
# 어차피 첫자리가 큰수를 기준으로 정렬 -> 젤큰놈부터 앞에 넣어준다.
# *첫자리가 같은데, 2번째부터.. 34 3 33 같은 경우가 있는데,    34 > 3 > 30 순으로 정렬되려면, 
# 애초에 비교할 수 있는 최대자리수 4자리를 만들어서 비교해버리면 된다.
# -> 1자리수면 9 -> 9999로 여전히 젤 크게 유지된다.
# -> 2자리수면 4 34 3 30 3333-> 4444 3434 3333 3030 3333 -> 첫자리 큰 4는 젤 크게 되는 것도 여전하지만
# --> 문제는 3과 30과 3333 이다.
# -> 원본정렬에서도 3이 30보다 더 앞에 있어야한다. 왜냐면 3뒤에 30보다 0이 아닌 어떤수가 오더라도 30보다 크다.
# --> 3+a > 30 : a는 0이 될 수도 있기 때문에 예외처리를 해줘야한다...

#numbers = [str(n) for n in numbers] # 문자열로 변환.1개씩 str이므로, 반복문의 O(n)복잡도만 가진다.
# 변형된 데이터를 기준으로 정렬하도록 key에 준다.
#numbers.sort(key=lambda x:((x*4)[:4]), reverse=True)

numbers.sort(key=lambda x:((x*4)[:4], -len(x)), reverse=True)
# print(numbers)

ans = ''.join(numbers)
print(ans if ans[0]!='0' else'0')


