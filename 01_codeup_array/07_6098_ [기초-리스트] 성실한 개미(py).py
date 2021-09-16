## 느낀점 : while안에 다른변수 while시 break로 못벗어남. FlagOR변수로 챙겨놓고 해야할듯?
# -> flag없다면 2중 for문은 break로 못벗어나게됨.
# -> if문 반복처리 ->  업데이트되면서 while 을 쓰자.
# -> 여러 경우의 수 중 확실하게  끝나는 것부터 if return/ if break로 끝내놓고 if로 다시 시작하자.
# -> 넘어가기 전, 다음 것을 검사하나, 
#    다음 것 가능? -> 현재 것 check완료 정도의 계획을 세운다.
#    다음것OK? -> 현재 check완료(9) **못가더라도 도달한 상태면 9로 check완료로 해준다.** & 다음 것 좌표로 이동(x+1,y) or ( x, y+1)된 상태 -> 판단부터 하면되~
# -> while 반복문에서 // 현재 판단부터한다면?? 직전에서 업데이트만 시켜놓고// 판단은 담루프의 판단부터 시작
# 9: 다음것 가능?이든 말든 직전에 update됬으면 넣어줄 것
# 1 : 못가는 특별한 경우 -> 0과 2는 갈 수 있으니 1만 따로 처리한다.
# 2 : 다음것 0or2로 넘어왔다면? 2는 완료처리. 탈출처리를 반복문 맨처음에. 0은 다음루프돌도록 update만 함.
# -> 탈출조건이라도, 0과 2는 1과 구분해서 같이 묶어서 가도된다.
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################
# data = list(map(int, input().split()))


data = [list(map(int, input().split())) for _ in range(10)]
# pprint(data)



x = 1
y = 1
data[x][y]=9
locations = [] 


# while x<=8 and y<= 8 :
#     curr = data[x][y]
#     next_right = data[x][y+1]
#     next_bottom = data[x+1][y]
#     if next_right == 0:
#         y+=1
#         data[x][y]=9 #
#     elif next_right == 2:
#         y+=1
#         data[x][y]=9 #
#         break 
#     else:
#         if next_right==0:
#           y+=1
#           data[x][y]=9
#         elif next_bottom == 0:
#             x+=1
#             data[x][y]=9 #
#         elif next_bottom == 2:
#             x+=1
#             data[x][y]=9 #
#             break
#         else:
#           break

x, y= 1, 1

while x <= 8 and y <= 8:
    curr = data[x][y]
    next_right = data[x][y+1]
    next_bottom = data[x+1][y]

    # 탈출조건을 루프 젤 위에 적는다.
    # 넘어온 현재상태에서 판단한다.
    # -> 넘어가기 전,  다음 것을 검사하나,  현재것 check(9)-> 다음좌표로 넘겼음.
    # -> 다음 것 가능? -> 현재 것 check완료 정도의 계획을 세운다.
    if curr == 2:
        data[x][y] = 9
        break

    # 오른쪽 먼저 갈 수 있는지를 if문 상단에 올려서
    # 직전에  아래 간 상황이라도  (오른쪽?or아래쪽?) 선택지에서 오른쪽 먼저 갈 수 있으면 가게 된다.    
    if next_right != 1:
        data[x][y] = 9 #현재것 체크완료 다음좌표로 이동된 상태
        y+=1
    else:
    # 오른쪽은 못가는데...
        # 아래쪽은 가면? 가서 다음 루프 돌면 알아서 먼저 오른족 검사됨.
        # 아래쪽은 가능?에 0 or 2도 담겨있다. -
        # -> 더 적은 1을 if에 걸고, else에 0or2 -> 다음루프 처음에 판단
        # -> 담것 못가더라도.. 현재는 체크완료를 9를 넣어준다.
        if next_bottom == 1:
            data[x][y] = 9
            break
        # 아래쪽이 갈 수 있을 때  0or2 -> 2는 탈출조건이므로 담 루프첨에 해결된다.
        else:
            data[x][y] = 9
            x+=1
            

pprint(data)

    



    


    
