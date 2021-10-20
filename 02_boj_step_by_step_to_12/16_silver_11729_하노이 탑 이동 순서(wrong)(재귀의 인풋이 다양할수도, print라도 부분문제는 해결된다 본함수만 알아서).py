# 느낀점 : 
# - n by n-1뿐만 아니라... 다른요소들까지 부분문제에서 달라지면(start, end기둥) 인자로 받아줘야한다.
# - 각 부분문에서 return으로 끝내는 대신 print 이동경로를 출력함. 
# - 3수 고정 -> 3수의 합 고정 -> 2개 알면 1개 추론 가능.
# - n-1 / print / n-1이며, 부분문제에서 알아서 hanoi(n-1)도 출력될 것이다.. 
# **- 부분문제 정복 n-1에서도 이미 내부 구조가 있기 때문에 ---> n상황에서만 print를 하면, 알아서 또 재귀적으로 print될 것임.**

################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################

N= int(input()) 

# hanoi (n)번째는,, 1->3으로 가는데
# hanoi(n-1)을 1->2번기둥으로 -> n번째원판 1->3으로 -> hanoi(n-1)를 2->3으로 한번더 

# 1) 맨 밑 원판 제외 start -> other
# 2) 맨 밑 원판 start->end 
# 3) 제외원판 other -> end  
# 4) 1->3으로 갈때는 2 ,  2->3으로 갈때는1, start -> end로 갈 때는 6-(start+end)
#  -> 3수가 일정 = 3수의 합이 일정 -> 나머지 1개 추론가능

count_list = []
def hanoi(n, start, end):
    
    if n == 1:
        # start, end는 뭐가올지.. 점화식에서 결정되니.. 그것을 출렴난 해주자. 그리고 종료까지..?
        #print(start, end)
        count_list.append((start, end))
        return

    # n-1을 처음에 end가 아닌  다른기둥에 옮겨야한다.
    other = 6-(start+end)
    hanoi(n-1, start, other) 
    #print(start, end)
    count_list.append((start, end))
    hanoi(n-1, other, end) 


hanoi(N, 1, 3)
print(len(count_list))
for data in count_list:
    print(*data)




    