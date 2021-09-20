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