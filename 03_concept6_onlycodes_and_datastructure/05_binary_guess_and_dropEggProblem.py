#### 스무고개: 전체범위에서 중간값[mid]가지고 정답인지 물어보면서 
#             탐색범위를 절반으로 줄여나간다. start == end가 될때까지 중간에 답이 나와도, 새로운 mid로 찾아나간다.
#     - 과정은 이진탐색같지만, 답이 나와도 쌩까다가 start==end의 최악의 상황만 정답으로 친다.
#     -- if mid == answer: return mid (break)가 생략된 [이진탐색 다도는 최악의 상황]이 스무고개다.
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
print("1. binary_guess(): 스무고개란? if mid == answer:break, return처리 없이 이정배씨 이진탐색 다돌기 100% 탐색됨?? >>> ")

for _ in range(10000):
    answer = random.randint(start, end)
    guess = binary_guess(answer, start, end)
    if answer != guess:
        print("   스무고개로 찾은 정답과 실제 정답이 다릅니다.")
        break 
else: 
    print("   스무고개(이진탐색 모든루프돌아야 start==end)는 100% 답 찾아냄")


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


print("2. binary_guess_count(): 스무고개(이진탐색 종료까지 다돌기)는 최초범위(1,1000)에 대해, answer에 따라 몇번을 돌까?")
print("  1을 찾을 때 >>>", binary_guess_count(1, 1, 1000))
print("  500을 찾을 때 >>>", binary_guess_count(500, 1, 1000))
print("  700을 찾을 때 >>>", binary_guess_count(700, 1, 1000))
print("  750을 찾을 때 >>>", binary_guess_count(750, 1, 1000))
print("  1000을 찾을 때 >>>", binary_guess_count(1000, 1, 1000))
# 1 찾을 때 >>> 10
# 500을 찾을 때 >>> 9
# 700을 찾을 때 >>> 10
# 750을 찾을 때 >>> 9
# 1000을 찾을 때 >>> 9
# my) 
print("  mid==answer의 예외처리가 없어 중도에 답찾아도 = 정답이 start or end에 있어도, 새로운 mid로 값으로 물어보면서 찾아가며")
print("  정답이 중간값에 걸리게 되면 1번 일찍 찾는다. 1~1000 찾기는 9번 or 최대 10번")
print("  이진탐색이라면, while문을 도는 와중에 mid == answer가 되면 탈출하고 반환하도록 해야한다.")
print("  스무고개는 이진탐색의 최대 몇번??까지 물어야 마지막 1개로서 찾냐?의 이진탐색 최악의 상황을 말하는 것 같다.")


print("3. 탐색범위(1,1000 -> 1,n)에 따라 binary_guess_count()는 어떻게 달라질까?")
start = 1 
#end = [ 2**n for n in range(21) ] # [1, 2, 4, 8, 16, 32, 64, 128,
# 각 end마다 1000개씩을 테스트하면 (9or10처럼) 가장 최악의 상황은 몇번 물어야하는 걸까?
for end in [ 2**n for n in range(10) ]:
    # 각 end마다 1000번을 확인해서 max_count를 update해서 찾아놓는다.
    max_count = 0
    for _ in range(1000):
        answer = random.randint(start, end) 
        count = binary_guess_count(answer, start, end)
        max_count = max(max_count, count )
    print(f"  현재 (1, {end})까지 스무고개(이진탐색최악)로 물어보는 횟수는 최대: {max_count}번입니다.")
print(">>> 1~n 까지 스무고개(이진탐색최악) 최대 질문수(횟수)는 lg2(n)개 필요하다. 반대로 1~2^k -> 질문k번 필요")



#### 계란 낙하문제
# - 1~n까지 층 가운데, 계란이 깨지는 층 T를 찾는 문제다.
# - 1,n중에 answer를 1개를 찾는 것은, [이]미 [정]렬된 [배]열이므로 [이진탐색]으로 탐색범위를 절반씩 줄여가면 된다.

print("4-1. isSafe(height) : 계란 = 질문 = 목숨이 무효처리로 살아날 수 있는지>>> ")
# 4-1. 내가 선택한 층(옛 mid)와 깨지는 층(옛 answer)의 비교로 구간을 좁혀가기전에
#      대소비교를 통해,  1) height < answer : 안깨짐. 살음. 질문무효 
#      vs  2) height >= answer : 깨짐, 질문처리됨. 의 T/F판단을 먼저해보자.
#      why? 구간좁혀가는 조건문을 T/F로 처리할까?
import random

n = 100
answer = random.randint(1, n)

def isSafe(height):
    if height < answer:
        return True 
    else: # height >= answer 
        return False 
print("  깨지는 층 answer >>>", answer)
print("  isSafe(55) >>>", isSafe(55))
print("  isSafe(3) >>>", isSafe(3))

    

# 4-2. 계란(질문)이 하나인 경우? 
# - 목숨이 1개이기 때문에, 중간값을 던져서 줄이는 이진탐색(count lg2(N)번 필요) 못한다.
# - 1층부터 순차적으로 가다가 isSafe == False의 깨지는 순간이 정답순간
# - 이진탐색을 못하니, T층까지는 T번이 걸림. 
# - 제한범위 n을 인자로 받아서, 거기까지 돌면서, 깨져서 걸리면 return하고 끝
def eggDrop1(n):
    for height in range(1, n+1):
        # 안전하다면 height가 for로 자동으로 계속+1씩 올라가고, 안전하지 않다=깨지면 return하고 끝
        if not isSafe(height):
            return height
        
print("4-2. 답:", answer, "eggDrop1(n)) >>>", eggDrop1(100))


# 4-3. 계란이 많은 경우?
# - 계란 = 질문 = 목숨수가 많다보면, 이정배 상황에서는 정답까지 효율적으로 찾아가려고 -> 이진탐색을 쓸 것이다.
# **일반 이진탐색과는 다르게 start==end를 붙이는게 아니라 [start안깨짐][end깨짐]상태로 종료 시키고 싶다.**
# **반복문을 다 돌면, [start==answer범위에 안들어가게 업뎃][end== answer일 수밖에 없음] 2개를 남기면서, end가 answer일 수 밖에 없도록 업뎃시킨다.**
# - 1) 이진탐색X : 중간에 mid == answer확인시 종료 없음. -> while을 다 돌아야함.
# - 2) start == end가 끝이 아님: start는 answer가 될 가능성 없도록 업데이트
#      2-1) start+1 == end일때까지로 제한하여 돌린다  -> while start+1 < end   [start][end]상황 유지
#      2-2) mid < answer 상황에서 start뒤로 땡겨 update시 :  start = mid+1 (X)   start = mid (O) 안닿게 업데이트
def eggDrop2(n):
    start = 1
    end = n
    while start + 1 < end:
        mid = (start + end)//2
        
        if isSafe(mid): # mid가 안전?   mid < answer -> start 업뎃해야함 -> 안닿게 업뎃
            start = mid
        else:# mid가 깨짐? mid >= answer -> end를 앞으로 update + answer에 닫도록
            end = mid 
        
    # 다 돌고나면, [start][end]상태이며, start는 answer가 안되므로 end가 answer임.
    return end 

print("4-3. 계란이 많은 경우, 정답 찾아보기:eggDrop2(n)) >>>", eggDrop2(100))
