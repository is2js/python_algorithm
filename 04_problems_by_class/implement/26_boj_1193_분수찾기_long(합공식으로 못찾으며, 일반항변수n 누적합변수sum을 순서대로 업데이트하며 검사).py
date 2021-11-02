# 느낀점:
# *1. X=n*(n+1)/2를 만족하는 n을 구하려고 하는데, for로 1씩 대입을 하고 싶어도 언제끝나는지 모름 -> while
# **-> while + n으로 가면서  + An을 누적해서 만든 Sn -> if Sn >=X까지 반복하다가 break해서 그때의 n을 찾아야한다.
# * -> 끝을 모르니 while문에 n=0 부터 시작해서 n+=1로 합공식X 일반항을 누적해서 돌린다.
# *2. while 문에 들어갈 검사조건에 들어가는 변수는 누적합이며 cumsum+=n으로서, cumsum이 검사된다.
# * -> 검사변소cumsum을 업데이트하기전에, <미리 n 등을 update하고 ->검사변수 cumsum을 update해야지 while탈출후 돌아가기를 안해도 된다.>
# ** -> n을 한번 업데이트 시키고 들어가려면, n=0으로 초기화해놓고 n = n+1 이후 cumsum = cumsum+n    의 방식으로 짠다.
# *3. n번째 군집의 몇번째인지 알기 위해서는
# 3-1. 군집의갯수 변수 n 초기화후 update
# 3-2. 군집갯수누적합 & 검사 변수 cumsum  초기화후 update 하도록 2개를 선언해야한다.
# 3-3. cumsum으로 검사할 것이기 때문에, 그 전에 n이 update를 끝내도록 해야 편하다. 
#     * -> 당시의 n을 while탈출후 사용할 수 있다.



################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# ######################################################

X = int(input())

# * 1. 자체 군집이 있으며, < 그 군집의 몇번째에 해당 >하는지 찾아야한다.
# 1-0 끝을 모르니 for문 대신.. while 조건문
# 1-1 [k번째 군집의 갯수] 업데이트 -> 해당 군집의 갯수를 알아야 그때의 누적합도 업데이트하지.
# 1-2 [k번째 군집까지의 합]을 update할 변수.. for처럼.. 직전까지의 -> 현재항을 이용해서 업데이트

# cluster = 1
# cluster_cumsum = 0
# # *2. 군집들이 누적되다가,, X를 넘어서는 <=  cumsum포함하는 군집에서 직전까지
# # if X <=cluster_cumsum :
# while X > cluster_cumsum : # 계속 X가 크다가.. 작거나 같아지는 순간 멈춘다.ㄴ
#     # (작다가) 같아지는 순간  -----X=cumsum]
#     # (작다가) 커지는 순간   --X---cumsum]
#     # 저 순간에 탈출한다.
#     cluster_cumsum = cluster_cumsum + cluster
#     cluster = cluster+1
#     # * 후증가였다면.. <업데이트 전 cluster를 사용한 cumsum이 빠젼나옴 -> cluster는 한단계 더 간것 >빠져나온 순간.. cluster는 한번 더 업데이트 된 상황 -> 돌린다.
#     # 0부터 시작해서 선증가였으면 1단계 안돌려도 된다?
# print(X, cluster, cluster_cumsum)


cluster = 0
cluster_cumsum = 0
while X > cluster_cumsum : 
    # * 업데이트이후의 값을 활용해서 통과, 즉, 업데이트 -> 업데이트 변수로 활용 검사 -> 탈출  ->  증가상태가 아님!
    cluster = cluster+1  
    # * while 검사 받는 변수는, 업데이트 된 변수를 쓰도록 맨 나중에 업데이트하면
    # ** 탈출후 업데이트의 전으로 조절하는 수고가 없다.
    # -> 이 cluster+=1 이후 누적합이 되도록 -> 초기값을 0, 0으로 하자.
    # * 누적되는 변수, 누적합 변수는 -> whlie문 들어가기전에 최초 업데이트 필요한 상태로 만들어놓자.
    # -> ex> 1부터 시작-> 0을 담아놓고 -> while문에서 업데이트 하고  -> 누적합 -> 검사
    cluster_cumsum = cluster_cumsum + cluster

# print(X, cluster, cluster_cumsum)

# * X가 k번 군집에서 몇번째인지 알려면
# 누적합 - 현재군집(현재 cluster) = 직전까지의 군집 누적합을 알아야함
k = X-(cluster_cumsum - cluster)

if not cluster%2 :
    a = cluster+1-k 
    b = k
else:
    a = k
    b = cluster+1-k 

print(f"{b}/{a}")







# # 1. X가  (1 + 2 + 3 ) 처럼 커지고 있는 가운데 몇번째 그룹인지 확인해야한다.

# #  1부터 대입하면서 k번재 그룹을 찾는다?
# cumsum = 0 # 그룹의 누적합.
# cnt = 0 # 돌아가는 각 그룹
# while cumsum < X: # 누적합이 X보다 크거나 같은 순간 빠져나온다.
#     cnt+=1
#     cumsum+=cnt
# # 딱 걸려서 끝난 경우, [   X]
# # 누적합이 X를 넘어선 경우,   cnt-1]  [ ----X---cnt]
# # 똑같네.. 
# print(X, cnt, cumsum)

# # x의 그룹내 번째..-> 직전그룹까지를 빼면 된다.
# nth = X - (cumsum - cnt)

# if not cnt%2 :
#     #뒤에서부터 (그룹넘버+1-k)/k
#     print(cnt+1-nth , "/", nth)
# else:
#     #앞에서부터  (그룹넘버+1-k)/k
#     print((cnt+1-nth) , "/" ,nth)


# # if not cnt%2


    

# sum_group = 0
# for i in range(1, k):
#     sum_group += i
#     if 