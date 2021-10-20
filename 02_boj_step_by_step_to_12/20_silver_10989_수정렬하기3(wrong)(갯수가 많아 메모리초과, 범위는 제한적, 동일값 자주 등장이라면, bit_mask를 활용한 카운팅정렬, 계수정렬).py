# 느낀점 : https://velog.io/@minzz/BOJ-1018%EB%B2%88-%EC%B2%B4%EC%8A%A4%ED%8C%90-%EB%8B%A4%EC%8B%9C-%EC%B9%A0%ED%95%98%EA%B8%B0-Python
# - 시간과 메모리제한(8M)이 있는 경우 -> 최대 100만개의 데이터를 변수(배열)에 저장하면 안된다.
# **들어오는 범위(index로 들어가자)가 갯수(메모리초과야기)에 비해 작고, 같은 것이 반복(index의 value에 +=1씩 시키자)되어 누적시킬 수 있다면, bit_mask를 활용한 카운팅 정렬**
# --> 갯수가 엄청 많이 주어지면, 배열로 받지말고, 들어올때마다 mask에 +1씩 누적되도록 하자.
# --> 미리 오름차순인 index에 매칭되는 bit_mask에 표기한다.
# - [문제조건인 - 범위내숫자 - 10000이하 자연수]라서 bit_mask 0~9999까지 미리 배열을 생성해놓고, +1의 표기만 한다.
# - 만약 0에 +2가 되어있다? -> 1이 2개 들어왔다. -> 0이 아닐 경우 + n개만큼 1을 출력하면, 정렬순으로 배열하는 것이 됨.
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
############################
import sys
N = int(sys.stdin.readline())

bit_mask = [0 for _ in range(10000)]
#data = [ int(sys.stdin.readline()) for _ in range(N)]
for _ in range(N):
    index_1 = int(sys.stdin.readline())-1
    bit_mask[index_1] +=1
    
for i in range(len(bit_mask)):
    if bit_mask[i]:
        for _ in range(bit_mask[i]):
            print(i+1)    
