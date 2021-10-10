x = 78696
y = 19332

# 소인수를 구할 때, 2~n-1까지 소수를 먼저 구하는 후보들 모은 것보다
# 2부터 +1씩 증가시켜도, ~루트(n)까지만 조사하면 다 나오고 빠르다.
# 대신, 루트(n)이후에 나오는 짝의 소인수는 챙겨줘야한다(나눠지기전에 루프가 끝남.)
def factorize2(n):
    factors = [] 
    factor = 2 
    while factor ** 2 <= n : 
        while n % factor == 0:
            factors.append(factor) 
            n = n//factor
        factor+=1
    if n>1:
        factors.append(n)
    return factors


print('❤1 factorize2(x) >',factorize2(x))


# commFactors with factorize2(): 공통 소인수 찾아내는 로직(-> 누적곱시 gcd가 될예쩡) 
def commonFactors(factorized_list1, factorized_list2):
    i, j= 0, 0 
    commons = [] 

    while i < len(factorized_list1) and j < len(factorized_list1):
        if factorized_list1[i] == factorized_list2[j]:
            commons.append(factorized_list1[i])
            i+=1
            j+=1
        elif factorized_list1[i] > factorized_list2[j]:
            j+=1
        else:
            i+=1
    return commons

print(f'❤2 commFactors(factorize2({x}),factorize2({y})) : ',commonFactors(factorize2(x), factorize2(y)))


# 3. gcd2 with factorize2, commFactors
def gcd2(n, m):
    f_n = factorize2(n)
    f_m = factorize2(m)
    factors = commonFactors(f_n, f_m)

    gcd=1
    for i in factors:
        gcd*=i
    return gcd

print(f'❤3 gcd2({x},{y}) with factorize2, commFactors: ', gcd2(x, y))


# 4. lcm : 최소공배수 풀기1 - 두 수의 곱과 gcd만 알면 (gcd*a*b인 lcm을) 바로 구한다.
# A = GCD * a  / B = GCD * b  
# -> A*B = GCD^2 * a * b -> 두 수의 곱에서 gcd 한번만 나눠주면 lcm이다.
# lcm = GCD * a * b  =========   A*B/GCD
# -> gcd는 math모듈에서 쉽게 추출할 수 있다.
import math

def lcm(m,n):
    return (m*n) // math.gcd(m,n)

print(f'❤4 lcm({x},{y}) with math.gcd: ', lcm(x, y))


# 5. 1부터 10까지 lcm은?
# - 공간최적화처럼 업데이트한다. 돌면서 어딘지는 모르지만 min(,) max(,)를 찾아냈던 것처럼..
# - 직전까지의 lcm.. for문안에서는 현재의 lcm으로 업데이트시켜주면서 돌기..
# - curr(현재의) <- func( curr(직전까지의), new)
# - 어떤 값이 있고, 추가된 숫자로 계싼을 한뒤, 해당 변수에 update시키는 누적계산
# -- 변수1 for  변수1 = 계산(변수1, 새로운값)  -> 변수1을 최신으로 update
# -- 변수이자 결과값을 담는 곳-> 현재로 업데이트

curr_lcm = 1
for i in range(2, 10+1):
    curr_lcm = lcm(curr_lcm, i)
print(curr_lcm)

def lcm_from_to(start, end):
    curr = start 
    for num in range(start+1, end+1):
        curr = lcm(curr, num)

    return curr 

print(f'5 lcm_from_to(1,10) with math.gcd: ', lcm_from_to(1,10))


# 6. lcm2 with lcmFactors : 두수의 곱과 gcd를 이용한 쉽게 푸는 방법이 아니라
#    소인수분해후, 인수를 뽑아내서 최소공배수를 만들어보자.
# - 최대_공약수 : 소인수분해후 공통이면 다 뽑아내기(작은것을 버리고 큰쪽에서 기다림)
# - 최소_공배수 : 소인수분해후 lcm에 해당하는 GCD + a + b 다 뽑아내기
#   -> 작은 것도 안버리고 챙긴다. a or b 에 해당할 것이기 때문.
#  2-2 2-2 [2]-3 3-3 4-[3]  -> 2와 3을 버려야할 것 같지만, GCD외에 전부 a, b에 해당하므로 챙겨야한다.

def lcmFactors(factorized_n,factorized_m):
    factors = []
    i, j = 0, 0
    # 조건이 2개가 and로 걸려있으면 -> 어느것이 끝나서 종료되었는지 나중에 확인
    while i < len(factorized_n) and j < len(factorized_m):
        if factorized_n[i] == factorized_m[j]:
            factors.append(factorized_n[i])
            i+=1
            j+=1
        elif factorized_n[i] < factorized_m[j]:
            factors.append(factorized_n[i])
            i+=1
        else:
            factors.append(factorized_m[j])
            j+=1

    # 아직 안끝났다면.. 챙겨라.
    if i < len(factorized_n):
        factors.extend(factorized_n[i:])
    if j < len(factorized_m):
        factors.extend(factorized_m[j:])

    return factors

print(f'6-1 lcmFactors([1,2,3],[2,3,5]) with factorize2 아직 lcm되기엔 누접곱이 남음.: ', lcmFactors([1,2,3],[2,3,5]))

# 6-2. lcm2 with factorize2 + lcmFactors 
def lcm2(n,m):
    f1 = factorize2(n)
    f2 = factorize2(m)
    factors = lcmFactors(f1, f2)
    # [ GCD 1개, a들, b들] -> 누적곱해야함.

    curr = factors[0]
    for i in factors[1:]:
        curr*=i
    return curr


print(f'6-2 lcm2(10,12) with lcmFactors : ', lcm2(10, 12))








