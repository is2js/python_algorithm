# 느낀점: 
# *1. stack에서 추가조건(pop횟수제한)은 while의 제일 마지막에 조건을 주고 -> if 예외 살피자.
# *2. 배열에서 뒤쪽k개를 제거 -> [:-k] 슬라이싱으로 해결하기
# *3. 문자열숫자를 붙혀 큰수 만들기에서 2자리이상나올때 vs 1자리만 붙일 때-> stack으로 직전수와 비교하여 재배열한다

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



