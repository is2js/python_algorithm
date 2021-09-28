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



