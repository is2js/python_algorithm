
# 1. 년월일에서 +1000일 계산은?
# -> 제일 작은 단위(일) +1 후 판단 -> 다음단위(달)+1 , 일=1초기화 -> 다다음단위 판단 
# -> 제일 작은 단위의 판단 경우의 수
# 28일 
# 29일
# 30일
# 31일 -> 튀어나온 31일이 가장 많다. 1,3,5,7,[8],10,12
#  -> 30일은 그외에 2,4,6,9,11 중 2를 제외한 [4,6,9,11]
#  -> 29일은 [2월 중 윤년O에만]
#  -> 28일은 [2월 중 윤년아닐땐 28일]

y = 2020
m = 7
d = 9

# for _ in range(1000):
    # d+=1
    #if d > 31:
    #if d > 30:
    #if d > 29:
    #if d > 28: -> 판단기준 m에 의해 정해짐.(여러 경우의수를 가져 바로작성불가)
    # **1-1. 판단을 할때, 그 판단기준이 (다른변수에 의해)경우의 수를 가지는 경우,**
    # **내부에서 판단되서 1개의 판단기준을 뱉어내도록 함수로 정의한다.**
    #if invalidDay():

def leapyear(y):
    if ((y % 4==0) and (y%100!=0)) or y%400==0:
        return True
    else:
        return False

def is_invalid_day(y, m, d):
    # **경우의수가 너무 많은 경우, 그냥 default값으로 주자.**
    num_of_days = 31 # m == 1,3,5,7,8,10,12
    if m in [4,6,9,11]:
        num_of_days = 30
    
    if m == 2:
        if leapyear(y):
            num_of_days = 29 
        else:
            num_of_days = 28

    # 경우의수를 거쳐 판단기준이 나왔다. 그냥 여기서 판단해서 T/F로 반환하자.
    if d > num_of_days:
        return True # Day가 invalid하냐? 하다.
    else:
        return False 

for _ in range(1000):
    d+=1
    if is_invalid_day(y,m,d):
        m+=1
        d=1
        if m>12:
            y+=1
            m=1



# 2. 내장모듈 datetime으로 확인해보기
import datetime

# print(datetime.date(2020, 7, 9) + datetime.timedelta(1000))




#### 달력 만들기
# 1. 해당 년-월에 -> 모두 몇일인지?
# 2. 시작하는 1일의 요일 -> 무슨 요일에 시작하는지? 
# - 로직에서는 2가지를 알아야한다.
# - 일월활수목금토 순으로 출력하며, 한글은 2칸을 차지 + 좌우공백 / 숫자가 10이하라면 1칸을 차히자므로 왼쪽2칸공백+숫자+우공백1 => 하루당 각 4칸씩 차지하게 작성한다.

year = 2021
month = 9

day_of_week = 3 # 일월화수 0123  3부터 시작한다. 정사각형보다 +3칸 전진해서 시작하면... 나중에 7의배수에 넘어가는 것을 조금 덜가고 넘어가게 된다.
weekdays = list("일월화수목금토")

print(f"{year}년 {month}월")

