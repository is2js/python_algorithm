## 느낀점 : while안에 다른변수 while 넣음녀 안됨..ㅠㅠ 
# -> flag없다면 2중 for문은 break로 못벗어나게됨.


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
data[x][y]=9
locations = [] 


while x<=8 and y<= 8 :
    curr = data[x][y]
    next_right = data[x][y+1]
    next_bottom = data[x+1][y]
    # x판단
    if next_right == 0:
        y+=1
        data[x][y]=9 #
    elif next_right == 2:
        y+=1
        #rint("찾음")
        data[x][y]=9 #
        break 
    else:
        #print("y+1(right)막혔서 못갔음. x+1보기")
        if next_right==0:
          y+=1
          data[x][y]=9
        elif next_bottom == 0:
            x+=1
            data[x][y]=9 #
        elif next_bottom == 2:
            x+=1
            data[x][y]=9 #
            #print("찾음. y도 끝났따. flag?") 
            break
        else:
          #data[x][y]=9 #
          #print("y도 막혔으니 못가고 끝.막힌 것으로 끝.")
          break
        

pprint(data)

    



    


    
