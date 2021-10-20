# point#1 
# - 한탐뒤로 가서 i만 계산하고, count는 그대로 둘 것.(그 구간을 못채워도 현재 그 구간에 위치하고 있음)
# 구간먹기는 0부터 count하며, 
# 넘어서서 1타임 되돌아가는 것은 N이 구간을 넘어 몇번째인지를 구하기 위함이다.
# - 계산시만 N += 직전구간값 or  N - (구간count-1) *(구간길이) = i를 알아낸다.
# - 실제구간은 count에 있기 때문에 -1하면 안된다.

# point#2 
# - 길이가 딱 interval에 맞춰서 끝나는 경우 -> 
# 1) 한탐 뒤로 갈 필요없다 
# 2) interval이 일정하다면, interval자체가 i번째를 의미함
#    interval이 변한다면, 직전interval을 구해야할듯.

# point#3 구간 딱끝나는 경우 vs 남는 경우 가지로 나눠서.. 몫과 나머지를 이용한 풀이들이 많다.
# t = int(input())
# ​for i in range(t):
#     h, w, n = map(int, input().split())
    
# 1) 나머지가 0 == False가 아닌 경우 = 나머지가 있는 경우 = 딱 안맞아떨어지는 경우
# 구간으로 나눈 몫 == 구간count --> 나머지가 0이 아니므로 1구간 더 간다. (row+1)
# + 구간으로 나눈 나머지(i번재째의미) * 100(3자리수부터 자리를 차지하도록함.)
#     if(n % h): 
#         room = (n % h * 100) + (int(n / h) + 1)
# 2) 나머지가 False == 0으로 없는 경우 = 나누어 떨어지는 경우, 구간count = row, 
# i번재는 자동으로 구간길이
# 
#     else:
#         room = (h * 100) + int(n / h)
# ​
#     print(room)


# 내코드...

n = int(input().strip())
for _ in range(n):
    H, W, N = map(int, input().split()) # int - 2개
    # 호텔을 90도 왼쪽으로 돌린 행렬이라 생각하면, ||||| 세로의 H는 열의 길이 / W는 행수다.
    # N번째를 채우려면, 일단 몇행에 위치해있는지 알아야함. -> 구간이 열의 갯수만큼 이동됨
    interval = H 
    curr_row = 0 # 시작이 0행이 아니라 1행부터다..
    # N보다 같거나 넘어설 때, 끝난다. 
    # **같으면 해당row, 넘어서면 row-=1, N은 interval만큼 뒤로 접어주면서 N을 줄여나간다.**
    # N== 0생각해볼것
    while N > 0: 
        curr_row += 1
        N -= interval  

    # 만약, N==0딱 맞춰서 끝났다면? 해당 row의 마지막번재이므로, 한탐 더 뒤로 갈필요없이 현재row 상태에서, 
    # i번째를 정해야하는데,,, interval만큼 계속빼준 상태니.. N 자체가.. i가 된 상태다.. N>0이어야한다.
    if N == 0:
      # 딱 맞춰서 끝났다면..i는 딱 interval째다..
      N = interval
    else:
      # N<0라면.. 한탐 백업해서 막 >0 양수가 되었을때가 i다.
      N+=interval
      #curr_row-=1 # **한탐 빽업하는 것은, 구간후 몇번째 i인지를 구하는 과정이다. row(몇번째 구간)인지는 그대로 둬야한다. 줄이면 안됨!!!**
      
      

    # print(f"{row+1}행, {N}번째 >> {N}층 {row+1}호")
    print(f"{str(N)}{str(curr_row).rjust(2, '0')}")

 



