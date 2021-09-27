# 느낀점 : https://velog.io/@minzz/BOJ-1018%EB%B2%88-%EC%B2%B4%EC%8A%A4%ED%8C%90-%EB%8B%A4%EC%8B%9C-%EC%B9%A0%ED%95%98%EA%B8%B0-Python
# 1. n-1 + '666' 과 n-1=6부터는 '666'0~9까지 채우는 규칙은 발견하였으나
# 2. 너무 복잡한 조건은 그냥.. 해당안되라도 +1씩 시키면서 flag조건을 대조하여, 첨부터 카운팅 시키는 발상의 전환이 필요..
# 3. while에 조건이 들어갈 경우,  i < N 이라면,  i= N-1에서 들어가므로 i+=1을 먹어서 끝난다.
#    while조건에서는  i < N  :  <<< N까지 먹고나서 >>> 조건에 걸려서 끝난다.
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################
N = int(input())

# 조건별로 점점 세어 가는 것은 불가능.
# 그냥..통째로 while +1을 통해 -> Flag N번째 걸리면 break를 쓴다.
# - 조건:count가 == N이 될때까지 [666을 포함하는게 생길때마다 +1 counting] 반복. -> while 조건문에 걸던지,  or while True + flag
# - 횟수가 아니므로, i=0 <N은 별로안중요.
# - 문제에서 주어진 것에 의해.. 초기항은 잘 선택

# **숫자는 666이 등장하는 순간부터 시작하며, 666을 포함할시 < +1씩 시키면서 오름차순으로 모두 확인>한다.**
count = 1 # 종말숫자를 작은것부터 발견시 하나씩+1시킨다. -> 해당되는 N번째 종말 수를 flag로 빠져나옴.
number = 666 # +1씩 시키지만,, 첫째항으로 두고 이미 count=1부터 시작시키자.
# 이럴경우 N이 1이 와버리면.. 들어가기전에.. 끝나버려야하는데..
# <<< N까지 먹고나서 >>> 끝나므로 항상 N까지 가려면,[ while < N ]
while count < N : # if flag -> break보다는.. while문 자체를 [점점올라가는 정답발견count]를 조건으로 돌리자.
    number +=1
    if '666' in str(number):
        count+=1


print(number)