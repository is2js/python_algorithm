### 1. 소수 판단 with if 하나라도 걸리면 ->  flag + break
n = 11

is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False 
        break
print('1 >',is_prime)

### 1-2. 소수 판단 no flag -> if 하나라도 걸리면+ break + else 안그럼 ~
for i in range(2, n):
    if n % i == 0:
        print(f"{n} is composite number")
        break 
else:
    print("❤1-2 > prime Number")


### 2. 함수 isPrime() by if 하나라도 걸리면 (break->)return False  else True
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True
print('2 isPrime(n) >',isPrime(n))



### 3. 함수최적화 isPrime2() : 약수후보의 탐색범위를 2~n-1 -> 2~루트(n)의 곱의 중심까지
# - 약수존재범위를 2~n-1까지 아니라.. 어차피 존재한다면, 약수는 항상 짝으로 2 3 4 루트(24) 6 8 12 존재하니까 가운데 루트(n)까지 
# - n//2까지가 아니라... 짝은 곱으로 이루어지니... 루트(n)을 혼자서 2번 곱해지는 곱의 중심이라 생각한다.
# - range에는 정수만. -> 소수점 제거로 내림해준다.
import math 

def isPrime2(n):
    # for i in range(2, n):
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    else:
        return True
print('❤3 isPrime2(n) >',isPrime(n))



### 4. isPrime2 with if not isFlag함수: continue -> 중요작업
# - isFlag함수가 False면, 중요작업으로 내려가지말고 루프 건너뛰어라는 말.
# - 소수가 아니면 건너뛰고, 소수면 중요작업(append로  모으자)
print('4. if not Flag:continue -> 중요작업 : isPrime2함수로 소수만 모으기')
# Q. 2~100까지 소수는?
# - 내방식 : if Flag -> 바로 중요작업 
primes = []
for n in range(2, 100+1):
    if isPrime2(n):
        primes.append(n)

# - if not FLag + continue -> 중요작업
primes = []
for n in range(2, 100+1):
    if not isPrime2(n):
        continue 
    primes.append(n)
# print('4-2 if not continue >', *primes)

        





### 5. countPrimes(n) : 범위내 여러개의 소수를 셀땐 <처음부터 루트(n)탐색하는 isPrime2를 안쓰고> 다른 방법을 쓴다.
# - 1개의 숫자를 소수판단시 최적화된 isPrime2(n)라도, **범위내 여러개 소수 판단시 첨부터 탐색하는 함수는 안씀**, 다른 방식을 쓴다.
def countPrimes2(n):
    # index가 0(2) ~ n범위까지 판단해야할 범위 -> value가 T/F가 되도록 list를 사용한다.
    # - 판단해야할 범위를 index 중, 미리 초기항의 값을 주고 list + 연산으로 괄호떼서이어붙이기 to 판단해야할 갯수 맞출때까지
    # - 앞으로 누적되면서 반복되는.. 재귀같은 행동을 한다면?
    # -> 초기항에 해당하는 것 넣고 + for if True:count or 작업 등의 반복되는짓 + 그범위를 줄이는 작업
    sieve = [ False, False ] + [ True ] * (n-1)
    count = 0

    for i in range(2, n+1):
        if sieve[i]:
            count+=1
            for j in range(2*i, n+1,i):
                sieve[j] = False 
    return count

def findPrimes(n):
    sieve = [ False, False ] + [ True ] * (n-1)
    # count = 0
    primes = []

    for i in range(2, n+1):
        if sieve[i]:
            # count+=1
            primes.append(i)
            for j in range(2*i, n+1,i):
                sieve[j] = False 
    return primes


print('❤5 countPrimes2(n), findPrimes(n) 범위내판단 with New method(sieve:범위toIndex, 판단toValue), No isPrime -> No isPrime2 >', countPrimes2(11))
print('❤5 countPrimes2(n), findPrimes(n) 범위내판단 with New method(sieve:범위toIndex, 판단toValue), No isPrime -> No isPrime2 >', findPrimes(11))
print('❤5-cf) isPrime2(n)는 1개에 대한 Flag최적화 BUT 여러개(Primes)의 소수 판단시는 (매번 첨부터 도는 )Flag(Prime)안 씀.')


### 5. 
print('❤3 isPrime2(n) >',isPrime(n))