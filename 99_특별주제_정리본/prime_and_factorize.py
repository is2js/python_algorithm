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

        





### 5-1. countPrimes2(n) : by sieve(비트마스크) 범위내 여러개의 소수를 셀땐 <처음부터 루트(n)탐색하는 isPrime2를 안쓰고> 다른 방법을 쓴다.
# **1개의 숫자를 소수판단시 최적화된 isPrime2(n)라도, **범위내 여러개 소수 판단시 첨부터 탐색하는 함수는 안씀**, 다른 방식을 쓴다.
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

### 5-2. findPrimes(n) : 범위내 소수판단으로 개별판단(isPrime2(n))이 아닌 Sieve를 찾아서 소수 반환함.
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

print('❤5-1,2 countPrimes2(n), findPrimes(n) 범위내 소수 복수개 판단 with 범위를 index로 Sieve(범위toIndex, 판단toValue) >', countPrimes2(11))

 
### 6. factorize2(n) : 소인수분해 by 초기항(2) +1씩 루트(n)까지만 탐색(//factor) ->  n//factor로 합성수는 sieve 불꺼지듯이 다 지워졌기 때문에, 소인수들만 모인다. 마지막에 n>1인 경우를 챙겨줘야한다. 탐색범위를 벗어나서... 나눠줄순 없었지만, 불다꺼진이후 남은 소수기 때문이다.
# 6-1) factorize(n): findPrimes(n)-sieve이용+2~n까지의 소수들 모음을 이용하여 -> 후보 소수들 다뽑아놓고 약수인지 봄
# -    2~n-1까지의 소수들을 약수 후보로 선정한다(합성수 제외시킴)
# -   이 중에 약수(나누어떨어지는지)인지 확인하여 약수면 챙긴다. 즉, 약수 중 소수를... 소수들 다뽑아놓고 약수인지 봄
# -   해당 소수가 약수임이 확정되면 -> while 재귀조건문을 이용해 -> 안나누어떨어질때까지 계속 갯수를 그대로 챙긴다.
# -> 2로 나누어떨어지면, n//2를 다시 한번 2로 나누어떨어지는지 확인 -> 반복

# 6-2 factorize2(n) : 루트(n)까지 초기항에 +1씩으로 탐색(소수후보미리X) + 주의사항 : 마지막n의 몫이 1?(append ㄴㄴ) 아니면 덩어리?(-> 몫도 append해야할 소인수)
# --------소인수 분해 손으로 할 때 1이 남는경우/ 2~3 등 숫자가 남는 경우 나눠서 생각해보기
# --------factor line | n line 으로 손으로 쭉쭉 분해해나갈때, factor는 +1씩 루트(n)까지만 증가. 한 번 나눠떨어진 factor는 안나올때까지 계속 -> 
# -------- n은 n//factor로 기하급수적으로 주는데 반해, factor는+1씩 증가중이다. ->
# -------- 기하급수적으로 주는 n(n=n//factor)때문에 고정되서 점점커지는 factor가 탐색범위(루트(n)까지만)를 넘어서게 되어, n은 1까지 소인수분해가 되지 못하고 while문을 탈출하여 n=1보다 큰 수로 남아있다. 
# -------- 이때 남은 n은 소인수분해 한만큼하고 거기에 최초N = [fac,tor,들,] X [  ] 에 곱해져야할 소인수가 된다.
# --------- n//factor로 인해.. sieve 불이 꺼지듯 팍팍 값이 줄기 때문에, +1씩 커져봤자. 의미가 없이 금방 지나치면, 여기서 남게된 발견될 다음 factor들은 소수로만 이루어져있게 된다...
# ---------   1,3 (루트15), 5,15 -> 3만 챙긴상태로 탐색이 끝났어도.. n에는 5가 들어있으며.. 챙겨야한다.
# -> 소인수 후보들을 찾기위해, findPrimes(n)시..sieve를 이용한다지만, 소수를 미리 가려내는 것이 시간이 걸린다.
# -> sieve를 이용하더라도 2~n-1까지 소인수 **후보들을 미리 다 찾는 것**은 오래걸린다.
# -> 미리 후보 다찾고 확인?(X) -> **초기항(소수, 소인수는 초기항이 2)부터 확인**하면서 **소수만? ㄴㄴ +1씩 올리면서 해도 더 빠르게**찾기로 변경한다.
# -> 소수들을 건너뛰는 것보다. 각 항마다 //i 업데이트가 있으므로 +1씩 가면서 확확 줄여나가는게 더 빠르다고 함.
# -> 소수를 n까지가 아닌 루트(n)까지만 검색해도 이미 소인수분해가 끝나있다.
# -> 주의사항으로.. 확확 줄여나갈 때.. n = n//factor -> n은 1이 되면 그 전까지의 factor가 모두 소인수가 되며, 
#    1보다 더 큰값이 남아있을 때는, 루트(n)까지 탐색해도 나누어떨어지지 않으니, 그 수 자체를 소인수로 보자.
def factorize2(n):
    factors = [] # 손으로 소인수분해시.. 왼쪽 line.. 모아둘 소인수들..
    factor = 2 # 초기항2부터 n에다가 나눈 몫을 소인수로 취급한다. 

    # 구현) 탐색범위동안 반복을 위한 while  -> 단순 탐색은 i+=1 등으로 범위가 줄여나간다.
    #       이 문제에서는 내부while에 의해 n이 팍팍 줄어들어서... 최초 루트(n)보다 값이 점점 작아지는데..
    
    while factor ** 2 <= n : 
        # 구현) if재귀조건문을 대신하는 while : 업데이트가 팍팍되는 특징.
        while n % factor == 0:
            factors.append(factor) 
            n = n//factor
        # 할수있는만큼 반복되었으면, factor를 한 단계 높여줌
        factor+=1
    
    # 15 -> 3 x 5인데, 3까지만 하고.. 루트(15)-> 4보다 작아서.. 돌지못하고 끝났다.
    # -> 끝났으면 그냥 자동적으로 소인수은 탐색되었고, 나머지 쌩둥맞게 큰거만 따로 챙겨야한다.
    # -> 4 = 2 x 2 로 끝났으면 n은 1이 되어있다.  15 = 3 x 끝(5)에서 루트(n)을 넘어선 놈은.. 
    # n만 챙기면, 알아서 소인수가 뿌려진다. 왜냐면.. 루트(n)까지만 탐색(//factor)해도 합성수는 다 지워졌기 때문
    #  1,3 (루트15), 5,15 -> 3만 챙긴상태로 탐색이 끝났어도.. n에는 5가 들어있으며.. 챙겨야한다.
    if n>1:
        factors.append(n)

    return factors

         


print('❤6 factorize2(15) >',factorize2(15))


### 7. 
# print('❤3 isPrime2(n) >',isPrime(n))


