#### 스무고개: 전체범위에서 중간값[mid]가지고 정답인지 물어보면서 
#             탐색범위를 절반으로 줄여나간다. start == end가 될때까지 중간에 답이 나와도, 새로운 mid로 찾아나간다.
#     - 과정은 이진탐색같지만, 답이 나와도 쌩까다가 start==end의 최악의 상황만 정답으로 친다.
#     -- if mid == answer: return mid가 생략된 이진탐색 최악의 상황이 스무고개다.
#     - 정답을 모른다고 치고 random모듈로 난수를 생성한다.
import random 

def binary_guess(answer, start, end):
    # 원하는상태: start==end로서 1개의 값만 남은 상태
    # > while [not 정답상태] : [내부 원하는 상태로 가도록 update] ->  while 빠져나온 순간이 정답순간
    # 4) 정답이 될때까지 계속 반복하니 횟수는 모르는 상황이 됨.

    # 0) while [아직 not start == end] == [ start 아직 < end]
    while start < end: 
        # start==end로 가도록 중간값으로 update
        mid = (start+end)//2
        if mid < answer:
            # 1)start->mid+1로 땡겨서 줄이기
            start = mid+1 
        else:
            # 2) end -> mid로 땡겨서 줄이기
            end = mid

    # 3) 빠져나온 순간이 딱! 정답이 되는 상태: start==end상태
    return start 

start=1
end=1000
print("1. binary_guess(): 스무고개(중간값으로 범위반씩줄이되, 이진탐색최악 start==end일때만 정답으로)로 100% 찾을 수 있을까요? 1~1000사이 수 10000개로 test")

for _ in range(10000):
    answer = random.randint(start, end)
    guess = binary_guess(answer, start, end)
    if answer != guess:
        print("스무고개로 찾은 정답과 실제 정답이 다릅니다.")
        break 
else: 
    print("다 통과! binary_guess()로 1~1000를 모두(10000개) 찾았습니다.")


def binary_guess_count(answer, start, end):
    count = 0

    while start < end: 
        mid = (start+end)//2
        if mid < answer:
            start = mid+1 
        else:
            end = mid
        count+=1
    # 정답은 start == end로 찾은 상태니, 찾은 정답말고, while 몇번했는지 count만 반환
    # mid >= answer 상황 중 
    # mid == answer라도.. mid(정답) -> end(정답)로 바꾸고,  start+end(정답)//2 로 다시 mid(새값)으로 물어보니..
    # if mid == answer의 예외처리 안하는 이상.. 정답이 걸려있어도 범위좁혀서 중간값이 기준이 되어버린다.
    return count 


print("2. binary_guess_count(): 1~1000답은 무조건 찾는 스무고개는 몇번 물어(중간값이랑 비교) 보고 찾을까? ")
print("1을 찾을 때 >>>", binary_guess_count(1, 1, 1000))
print("500을 찾을 때 >>>", binary_guess_count(500, 1, 1000))
print("700을 찾을 때 >>>", binary_guess_count(700, 1, 1000))
print("750을 찾을 때 >>>", binary_guess_count(750, 1, 1000))
print("1000을 찾을 때 >>>", binary_guess_count(1000, 1, 1000))
# 1 찾을 때 >>> 10
# 500을 찾을 때 >>> 9
# 700을 찾을 때 >>> 10
# 750을 찾을 때 >>> 9
# 1000을 찾을 때 >>> 9
# my) 
print("  mid==answer의 예외처리 안해주면, 정답이 start or end에 있어도 새로운 mid로 값으로 물어보면서 찾아가며")
print("  정답이 중간값에 걸리게 되면 1번 일찍 찾는다. 1~1000 찾기는 9번 or 10번")
print("  이진탐색이라면, while문을 도는 와중에 mid == answer가 되면 탈출하고 반환하도록 해야한다.")
print("  스무고개는 이진탐색의 최대 몇번??까지 물어야 마지막 1개로서 찾냐?의 이진탐색 최악의 상황을 말하는 것 같다.")


print("3. 탐색범위(1,1000 -> 1,n)에 따라 binary_guess_count()는 어떻게 달라질까?")
start = 1 
#end = [ 2**n for n in range(21) ] # [1, 2, 4, 8, 16, 32, 64, 128,
# 각 end마다 1000개씩을 테스트하면 (9or10처럼) 가장 최악의 상황은 몇번 물어야하는 걸까?
for end in [ 2**n for n in range(21) ]:
    # 각 end마다 1000번을 확인해서 max_count를 update해서 찾아놓는다.
    max_count = 0
    for _ in range(1000):
        answer = random.randint(start, end)
        count = binary_guess_count(answer, start, end)
        max_count = max(max_count, count )
    print(f"  현재 (1, {end})까지 스무고개(이진탐색최악)로 물어보는 횟수는 최대: {max_count}번입니다.")
print(">>> 1~n 까지 스무고개(이진탐색최악) 횟수는 lg2(n) == 반대로 1~2^k -> 질문k번 필요")