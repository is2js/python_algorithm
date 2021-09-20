# 일단 나는 f-string으로 출력했기 때문에 소수점이 안찍혔는데
# python에서는 사칙연산(특히 나누기) 후 자동으로 실수형이 되니 출력시 int()로 찍을 것
# 5x + 3y = N 중. 5가 최대로 많게 하려면?
#  N%5 == 0 시 바로 출력
#  아니라면.. 3kg짜리 봉지 1개씩만 투입해야한다.
#  5x = N-3y에서, y를 1부터 증가해서 주고싶다. -> y를 증가안시키고 N에서 누적해서 빼면서 카운팅한다.
# ** 점화식에서 변수를 생성안하고 1부터대입하는 방법은  counting변수 + while  N-=3으로 계수를 누적해서 빼나가는 것고, counting한 것이 y값이 된다.**
# - 카운팅변수 + while + 누적 조합을 자주 생각하자.
# - 누적대상변수 N의 조건을 잘생각하자. 누적마이너스면, N>0이다. 문제조건은 N>=3이다. 문제조건에 따라 N<3일 때 실패다.

# - 제출전에 문제조건 + 0 대입까지 해보자.

# - 아래코드도.. 0넣으면 0이 출력된다.
# -> if N % 5 = 0이 while문에 겹친다. -> while 위 맨 위로 가져오고, 첫번째 검사후 N<3, 인 경우도 체크해준다.


if N % 5 == 0:
  print( int(N//5) )
else:
  count_three = 0
  while True :
    N-=3
    count_three+=1
    if N%5==0:
      print(int(N//5 + count_three))



### 내코드
# 점화식을 푸는데 시간이 오래걸림 + 문제조건을 지속적으로 볼 것. + while else문도 있다.
# - flag대신 for-else / while-else

N = Input.data

max_five, mod_five = divmod(N, 5)
max_three, mod_three = divmod(N, 3)
print(max_five, "<< 최대이자 첫 5의 갯수 ")
if N <= 0:
    print(-1)

if mod_five == 0:
  print(max_five, "5의 배수라서 끝")
# elif mod_three == 0:
#   print(mod_three, "3의 배수라서 끝")
else:
  # 5도, 3도 배수가 아니면, 5+3의 혼합이다.
  # N에서 5씩 줄이고 그 나머지가 3으로 나누어 떨어지는지 봐야한다.
  min_three = 0
  # 5의 몫이 첨부터 0인, 1,2,3,4는 ..5를 한번 못뺀다. N도 같이 5씩 줄여주기 때문에 N>0 조건이면 커버될듯.
  while N>0 and max_five >= 0:  
    k = (N - (5*max_five))
    if k % 3 == 0:
      min_three = k //3
      print(f"찾음 >>> {max_five} {min_three}")
      break   
    max_five -=1  
    min_three +=1 
    print(f"현재 max_five {max_five}  /  min_three {min_three}")
  else:
    print(f"다돌고  ==== 못찾았다 >> {-1}") 






# def func(n):
#   if n==3:
#     return 1
#   if n==5:
#     return 1 

#   if n-5 % 5 == 0:
#     return func(n-5) + 1
#   else:
#     return func(n-3)
#   return func(n-5)

# print(func(4))