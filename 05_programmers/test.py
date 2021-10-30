# 느낀점: 
# 이런식으로 풀어도 되는 이유는 "앞자리 숫자가 가장 큰 수가 큰 수"이기 때문입니다. 뭔 뜬금없이 당연한 소리야?라고 하실지 모르겠습니다. 문자열 어느 부분을 쪼갠다 하더라도, 앞자리가 높은 수가 되게끔 뽑으면, 무조건 높은 숫자가 된다는 것이죠. 즉, "앞자리를 최고 큰 수로 만들기 전략"이 부분해를 만족함과 동시에 전체의 해가 될 수 있는 것이지요.
#     collected = collected[:-k] if k>0 else collected #뒤에서 k개만큼의 글자를 끊어서 버림. 단, k가 0 이상일 때! k가 이미 0이면 그냥 collected를 반환.



def solution(number, k):
    stack  = []
    for n in number:
        # stack기본 조건 이외에, 추가조건은 맨마지막 and에 달아주자.
        # k=4부터 ~ 횟수라면 1까지 들어가도록 k>0
        while stack and stack[-1] < n and k>0:
            stack.pop()
            k-=1
        stack.append(n)
        
    # 특수조건을 for문 다돌고 확인한다?
    # stack에 뒤에서부터 한꺼번에 뺀다면, lst이므로 [:-k]를 쓰자! 굳이 계속 pop()할 필요없다.
    if k>0:
        # 1까지 들어가서 처리해줘야하니.. k=0일때 안되어야하니..
        stack = stack[:-k]
            
    return ''.join(stack)



