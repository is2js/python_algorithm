# 기존 풀이
# initial_number = '25'
# if len(initial_number)<2:
#     initial_number = '0'+ initial_number
# a,b = initial_number[0],initial_number[1]
# c = int(a) + int(b)
# k = str(b)[-1] + str(c)[-1]

# count = 1
# while initial_number != k:
#     #업데이트
#     if len(k)<2:
#         k = '0'+ k
#     a,b = k[0],k[1]
#     c = int(a) + int(b)
#     k = str(b)[-1] + str(c)[-1]    
#     count+=1
    
# print(count)
    

#  새로운 풀이
# 1. 일단 처음받은 수가 2번 필요하다면  a = b = n의 여러번 할당을 이용하자.
initial_number = n = int('55') # input()

# 2. while문 문제인데, cycle을 알기 위해 count=0을 선언하자. 
# - 후증가( 0 ->while 작업+업데이트+=1후-> 마지막 if검사) (count=0 -> while True: 작업후 업데이트 count+1 먼저 -> 내부에서 if문 검사 )
# - x선증가x( 작업 +1 -> while if 검사-> 업데이트 ) ( 선작업 -> count=1 -> while 먼저조건문: -> 작업후 업데이트+1)

count = 0 # 후증가1 - count 0부터 시작하기
while True: 
  # 후증가2 - 작업
  # my) n번째 자리수를 구하는 방법 : # print(2310 // (10**(n-1)) % 10)
  #   1) 그 자리수가 1의 자리에 오게 만든다. 10**(n-1)으로 나눈 몫(//)을 구한다.
  #   2) 1의 자리에 있는 수를 10으로 나눈나머지로 구한다 : % 10
  ten_num = (n // (10**(2-1))) % 10
  one_num = n % 10 
  next_num = ten_num+one_num 
  n = int(str(one_num%10) + str(next_num%10))
  
  # 후증가3 - 작업후 +1해주기
  count+=1

  # 후증가4 - 1상태에서 검사해주기
  if initial_number == n : 
    print(count)
    break
  
  
  
 