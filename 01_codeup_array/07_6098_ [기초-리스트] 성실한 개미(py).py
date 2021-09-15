################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################
# data = list(map(int, input().split()))


data = [list(map(int, input().split())) for _ in range(10)]
pprint(data)



x = 1
y = 1

locations = [] 

## 느낀점 : while안에 다른변수 while 넣음녀 안됨..ㅠㅠ break로 못벗어나게됨.

while x<=8 and y<= 8 :
    curr = data[x][y]
    next = data[x+1][y]
    next_y = data[x][y+1]
    # x판단
    if next == 0:
        x+=1
    elif next == 2:
        x+=1
        print("찾음")
        break 
    else :
        print("x+1막혔다.")
        while y<=8:
        # y 판단
            # x부터 먼저 살펴야함.. 막히지만 않으면 x판단으로 가얗됨.
            if next != 1:
                break 
            elif next_y == 0:
                y+=1
            elif next_y == 2:
                y+=1
                print("찾음. y도 끝났따. flag?") 
                break
        



    



    


    
