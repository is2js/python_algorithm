#### 콜라츠 
def collatz(n):
    seq = [n]

    while n>1: # n==1 일때 빠져나간다.
        if n%2==0:
            n = n//2
        else:
            n = n*3 + 1
        seq.append(n)

    return seq 

print("*1. collatz(10): 콜라츠 수열 생성 >>>", collatz(10))


print()

print("2. 1~100까지 콜라츠 수열의 길이만 >>")
for i in range(1,101):
    print(len(collatz(i)), end=" ")
print()
print()


print("3. index범위(X) 콜라츠 수열의 길이가 100인 숫자들 중 가장 작은 수는? 10번째 작은수는? >>>")
i=0
count = 0
while True: 
    i+=1
    if len(collatz(i))==100:
        count+=1
        if count == 10:
            print(count, i, collatz(i)[0])
            break
print()


print("4. 1~10000 사이에서 콜라츠 수열의 길이가 가장 긴 길이와 그 수는?? >>>")
max_len = 0
max_N = 1
for i in range(1, 10000+1):
    curr_len = len(collatz(i))
    #max_len = max(max_len, curr_len)
    if max_len <  curr_len:
        max_len = curr_len
        max_N = i

print(max_len, max_N)




#### 로마문자 -> 숫자
def toArabiNumber(roman):
    romanDict = {
        'M' : 1000,
        'D' : 500,
        'C' : 100,
        'L' : 50,
        'X' : 10,
        'V' : 5,
        'I' : 1,
    }
    arabic = 0
    for i in range(len(roman)):
        # i+1(다음항)과 비교할 때는, 조건을 먼저 달아주자. 맨 마지막index(n-1) 의 다음은 없으니 그 미만으로
        if (i < len(roman)-1) and romanDict[roman[i]] < romanDict[roman[i+1]]  :
            arabic -= romanDict[roman[i]]
        else:  
            arabic += romanDict[roman[i]] 

    return arabic
print("5. 로마숫자(문자)를 아라비아 숫자로 변환 toArabiNumber('CCLXIX')  >>>", toArabiNumber('CCLXIX'))


#### 아라비아 숫자 -> 로마문자
# 1) 큰 순서대로 단위 숫자보다 큰 경우, <<while로 단위보다 크거나 같은 동안은 반복해서>> 단위를 빼주면서 & 빈 문자열에 로마문자를 추가해준다.
# 2) 단위숫자보다 큰 감산법 ~ 그 다음 큰 단위숫보다는 작은, if 감산법 적용 구간(4, 9, 40, 90 등)이 나오면, 감산법을 먼저 처리하고(예외처리, 4, 9, 40, 90), else인 경우 단위숫자만큼 제거하고 문자열 추가해주는 작업을 하도록 한다.
# 3) 그렇게 만든 일자리, 10 ~99 , 100~ 변환함수들에서 패턴을 발견하여 종합한다.
#  -> 여러 단위가 있을 경우, 큰 단위 순서대로 <먼저(동전 같은 경우 sorted(, reverse)해서) 가진 동안은 계속 제거해주는 sense>
#  -> 종합시, 단위숫자 뿐만 아니라 감산법도 dict에 넣어서 예외처리와 단위숫자 제거를 같이하게한다.
#  -> 감산법 예외숫자(4, 9, 40..)가 여러번 제하여지면 어떻하지? -> 이미 그것보다 약간 큰 단위에서 짜를 만큼 짤라서.. 안됨..100으로 여러번 잘라놓으니.. 90은 한번밖에 안됨.

def toRomanNumber(n): 
    romanDict2 = {
        1:'I', 4:'IV',
        5:'V', 9:'IX',
        10:'X', 40:'XL',
        50:'L', 90:'XC',
        100:'C', 400:'CD',
        500:'D', 900:'CM',
        1000:'M',
    }
    str_=""
    for unit in sorted(romanDict2, reverse=True):
        while n >= unit:
            str_+=romanDict2[unit]
            n-=unit 
    return str_

print("6. 아라비아 숫자를 로마숫자(문자)로 변환 toRomanNumber(269) >>>", toRomanNumber(269))
