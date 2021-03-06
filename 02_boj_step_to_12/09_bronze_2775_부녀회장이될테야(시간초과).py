# point1 : 아래층 1~n호까지의 합이 바로 위값인데, 해당층-해당호직전값 = 아래층1~해당호까지의합 ->  아래층해당호값 만 더해주면,,
# - 즉,, k층n호의 값 -> k층 n-1호값 (왼쪽) + k-1층n호값(바로아래값) 을 더하면 만들어진다.
# - 점화식으로는 h,n = h,n-1 + h-1,n이다.
# - 2차 점화식은 행렬로 푼다. 문제에서 층과 호수가 0~14까지 밖에 없다. 만들어서 풀란 소리다.
# - 왼+아래 더해서 값을 점화식을 따라 1~14, 0~14를 돌면서 구하려면, 왼쪽 줄 전체(1열) 다1, 아래쪽 1행 1~i를 채워놓고 시작하면된다.

# 타인 답 풀이
#생각 1. 점화식을 구했으니, 이제 이차원 배열을 만들어서 그냥 처음부터 다 채워버리는게 좋을 것 같다.
#생각 2. 층 수는, 0층부터 14층까지 있고, 호수는 1호부터 14호까지있다. 왜냐면 문제 조건에 그렇게 나와있다.
#생각 3. 0층에 i호는 i명은 기본 조건, 각 층의 1호는 1명인것도 기본 조건 이 두개를 합쳐서 순차적으로 리스트를 채워나가면된다.

 
# 4층	1	6	21	56	126	252
# 3층	1	5	15	35	70	126
# 2층	1	4	10	20	35	56
# 1층	1	3	6	10	15	21
# 0층	1	2	3	4	5	6
#  	1호	2호	3호	4호	5호	6호

# lst = [[0 for j in range(14)] for i in range(15)] # 0부터14층, 1~n층
# for i in range(15): # 0열 채움(1호들 채움)
#     lst[i][0] = 1
# for h in range(14):
#     lst[0][h] = h+1 # 0행 채움(0층 1~14호까지 채움)
# 점화식을 x,y로 이용해서 푼다. 왼쪽+아래쪽을 더하면 다음게 나온다. 행렬을 다 채운다.
# for i in range(1,15):
#     for j in range(1,14):
#         lst[i][j] = lst[i][j - 1] + lst[i - 1][j]

# Test_case = int(input())
# for i in range(Test_case):
#     k = int(input())
#     n = int(input())
#     print(lst[k][n-1])


#############대박 #########
# 타인2 
# - list comp로 0층의 list를 만듬 [1,2,3,4..,n]
# - 누적합 행렬을 for i  f[i] += f[i-1]로써, i번째 요소는, 직전항을 누적해서.. 계속 누적해나간다.
# - 0층 행렬을 그대로 이용하면서, i번재에다가 i-1을 누적하는 방식이다. (전층의 값은 버리면서 계속 누적)
# -  0층 [1,2,3,4] 특히, i=1서부터 시작하여 첫째항빼고 누적한다. 게다가 i , i-1을 이용할 수 있게 된다.
# -  1층 [1,3,6,10] ... 와 대박.. 행렬 1개를 이렇게  list[i] += list[i-1]로 시그마를 구현
# t = int(input())

# for _ in range(t):  
#     floor = int(input())  # 층
#     num = int(input())  # 호
#     f0 = [x for x in range(1, num+1)]  # 0층 리스트
#     for k in range(floor):  # 층 수 만큼 반복
#         for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
#             f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
#     print(f0[-1])  # 가장 마지막 수 출력


# 나는...reduce를 써서 여러면 reduce를 반복하고 싶었는데
# for i in range(1, len(list)) :  list[i] += list[i-1] 로 직전항과의 합을 현재항으로 치환 -> 그걸 가면서 반복 -> 누적합으로 이루어진 list완성



# 내코드...

# - if 0층은 1~n까지 채운다.
# - for 각 층을 돌면서 for 각 호를 돌면서
# - 0번재 층은 i로 채운다. 각 호를 채울때마다 그 값을 다음층에 올려준다(행렬을 만들어서 거기에 채워둔다.)
# - k-1층까지 다음층위로  각 호까지의 누적합을 올려준다.
# - 각 호마다 누적합을 for 변수 for 에 누적할 수 있다. 
# - 각 호마다 누적합계산이 끝난 정보는 for 변수 for 2번재 for문끝에서 처리할 수 있다.
# - 0층만 i를 세워주고, 0층부터~k-1층까지는 각 호까지 모인 누적합을 위로 올려주면 된다.

# 4층 : sum(range(1,1) 1|1+(1)+(1+2)sum(range(1,1) + sum(range(1,1) + sum(range(1,1) + sum(range(1,2))
# 3층 : sum(range(1,1) 1|1+(1)+(1+2) sum(range(1,1) + sum(range(1,1) + sum(range(1,2)) |1+(1+2)
# 2층 : sum(range(1,1) 1|1+(1+2)sum(range(1,1) + sum(range(1,2)) |1+(1+2)+(1+2+3)   sum(range(1,1) + sum(range(1,2)) + sum(range(1,i))
# 1층 : sum(range(1,1) 1|1+2 sum(range(1,2))                     |<n*(n+1)/2>1+2+3 sum(range(1,i))
# 0층 : 1 | 2 | .. |n| ... 


# n 
# 0층 : i
# 1층 : 시그마(i)
# 2층 : 시그마(시그마(i))
# n층 : 시그마n-1번(i)
# from functools import reduce

# def reduce_floor(k,n):
#   return reduce(lambda x,y: x+y, list(range(1,n))) if k>1 else n 


누적합 = [ [0]*n for _ in range(k+1)]

total_of_floor = 0
for i in range(0,k+1):
  # print(f"k층 {i}>>>>")
  # 누적합 -> 
  floor_sum = 0 # 직전호까지의 누적합. -> 다돌면 각 층의 n호까지의 누적함.
  for j in range(1, n+1):
    # 0층일 땐 그냥 n을 차지하며, 
    if i ==0 :
      누적합[i][j-1] = j
    floor_sum+=누적합[i][j-1]  # 각 호실까지 누적합. 
    print(f"{i}층 {j}호 까지 누적: {floor_sum}")
    # 0층부터 ~ 마지막층아래까지 돌면서 위층에, 각 n호마다 현재층 누적합을 받아먹는다.
    if i<k:
      누적합[i+1][j-1]+= floor_sum

    # 0층끝났으면 1층 계산전에 1층 자리에 미리 올려두자. 0층 각 호실까지의 누적합을..
    # 올려주더라도.. 마지막층은 못올려준다.
    

# print(누적합)
print(누적합[k][n-1])
