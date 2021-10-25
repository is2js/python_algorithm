
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
        day=1
        if m>12:
            y+=1
            m=1



# 2. 내장모듈 datetime으로 확인해보기
import datetime

# print(datetime.date(2020, 7, 9) + datetime.timedelta(1000))




#### 달력 만들기
# 1. 해당 년-월에 -> 이번달은 몇일인지?
# 2. 시작하는 1일의 요일 -> 무슨 요일에 시작하는지? 
# - 로직에서는 2가지를 알아야한다.
# - 일월활수목금토 순으로 출력하며, 한글은 2칸을 차지 + 좌우공백 / 숫자가 10이하라면 1칸을 차히자므로 왼쪽2칸공백+숫자+우공백1 => 하루당 각 4칸씩 차지하게 작성한다.
# 1
year = 2021
month = 9
def leapyear(year):
    return (year%4==0 and year%100!=0) or year%400==0
print("1. leapyear(year) >>> ", leapyear(year))

def daysOfMonth(year, month):
    numOfDays = 31
    if month in [4,6,9,11]:
        numOfDays = 30
    elif month == 2:
        if leapyear(year):
            numOfDays = 29
        else:
            numOfDays = 28
    return numOfDays

print("2. daysOfMonth(year, month) >>> ", daysOfMonth(year, month))



year = 2021
month = 9

# 일월화수 0123  3부터 시작한다. 정사각형보다 +3칸 전진해서 시작하면... 
# 1) 전진횟수만큼 공백을 채우고 1이 시작되도록 출력한다.
# 2) 나중에 7의배수에 넘어가는 것을 조금 덜가고 넘어가게 된다.

day_of_week = 3 

weekdays = list("일월화수목금토")

print(f"{year}년 {month}월: ")
for day in weekdays: # 일월화수목금토 출력
    print(" "+day, end=" ")
print() # end =" "로 끝난 친구들다음에는 줄바꿀꺼면 넣어줘야함.
for _ in range(day_of_week): # 시작요일 전까지..전진횟수만큼 4칸씩 공백채우기
    print(" "*3, end=" ")

days_of_month = daysOfMonth(year, month)
for day in range(1, days_of_month + 1):
    if day < 10:
        print(" "*2 + str(day), end=" ")
    else:
        print(" "*1 + str(day), end= " ")

    if (day+day_of_week)%7==0:
        print()
    
print()

def dayOfWeek(y, m, day=1):
    t1 = y - (14-m)//12
    t2 = t1 + (t1//4) - (t1//100) + (t1//400)
    t3 = m + 12 * ((14-m) //12 ) -2 
    return (d + t2 + (31*t3 //12)) % 7
print("3. [암기]dayOfWeek(year, month, day=1) >>> ", dayOfWeek(year, month, day=1))


##### 다모은 달력
def printCalendar(year, month):
    day_of_week = dayOfWeek(year, month, day=1)
    days_of_month = daysOfMonth(year, month)
    weekdays = list("일월화수목금토")

    print(f"{year}년 {month}월:")
    for day in weekdays:
        print(" "+str(day), end=" ")
    print()
    
    for _ in range(day_of_week):
        print(' '*3, end=" ")

    for day in range(1, days_of_month+1):
        if day<10:
            print('  ' +str(day), end=' ')
        else:
            print(' ' +str(day), end=' ')
        if (day + day_of_week)%7==0:
            print()
    print()

print("4. printCalendar(year, month) >>> ", printCalendar(2021,9))
