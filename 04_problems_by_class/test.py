# 느낀점: 
# 1. 힙=우선순위큐는 최소값or최소값으로 변환될 수 있는 기준값(최대값 등)을 먼저 꺼낼 수 있으나, 중앙값은 한번에 꺼내지 못한다.
# * 2. 중앙값을 최소값으로 변환한 우선순위큐를 만들 순 없으나,  힙을 2개를 쓰면 -> [작은 그룹중 최대값 or 큰그룹 중 최소값] + [규칙]으로 중앙값 우선순위 큐를 만들 수 있다.
# * 3. 최소힙, 최대힙의 peek는 lst[0]으로 최소값, 최대값을 꺼내볼 수 있다.

# **4. **
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# 단계별로 푸시는 분: https://developer-ellen.tistory.com/33 # 고민 많이 하시는 분이라 챙겨놓음.
# 지져스 python 해설 블로그: https://peisea0830.tistory.com/category/BOJ # 해설&그림으로 미쳤음.
######################################################
# 해설1 : 지져스파이썬. https://peisea0830.tistory.com/59
# 문제: pop없이.. 그냥 들어오는 대로 중앙값을 뽑아내는 우선순위 큐를 생성.
# 1. 문제에서 짝수개일 때, 순서상 [abc][def]에서 , 중앙값은 왼쪽값(c)라고 했으며, <pop되지않으나 다음 중앙값후보가 왔을때, push전 비교대상>이므로 -> [작은그룹-최대힙에 insert되어야한다]
# 2. 중앙값은 1) 갯수가 항상 같도록 조정된다는 전제하에서는 2) 작은 그룹 중 최대값 or 큰 그룹에는 최소값으로 나타낼 수 있으며 3) 직전의 중앙값과 비교하여 그룹을 선택하여 입력하면 -> pop시  알아서 중앙값이 티어나온다?
# 3. 근데 순서가 보장되지 않으니 <우선순위큐=힙>을 이용한 heappush하여 알아서 <이진탐색으로>정렬 -> <이진탐색으로 pop> 되도록해야한다.
# 4. 또한 문제상 동일한 중앙값이 다시 들어올 수 도 있다.
#  [123] [45] <-- 3
#  4-1) 일단 갯수를 맞춰줘야한다. 그래서 우측(큰그룹에 최소힙)에 들어갈 수 밖에 없다. [123] [345]
#  4-2) 갯수가 짝수인 경우, 작은그룹에서 중앙값이 선택되어야한다. -> 작은그룹(최대힙) heappop  vs  큰그룹(최소힙) heappop을 비교해서 중앙값이 제대로 위치하도록 해야함.
#       12(3) (3)45의 비교이므로 아무거나 되어도 상관없지만, 
#      만일, [123][45] +2 --> [123] [245] --> 12(3) (2)45  라면? -->  4-1)갯수를 맞춰줘도  4-2) 중앙값후보 가운데 2개 ab(c) (d)ef 중  둘중 더 작은놈을 작은그룹으로 swap해줘야한다.
#  5. 만약, [12] [45] <-- 7 의 짝수개에서 삽입된다면?
#    * 잘은 모르지만, 먼저 경우에 생성한 규칙(작그룹max 와 큰그룹min을 swap  +  작그룹에서 중앙값이 나와야함.)을 적용해보자. 
#    1) 갯수는 맞춰질 순 없다. -> 그럼 어디 쪽에 삽입되어야할까?
#    2) 작은그룹에 삽입하면? <어디에 삽입되었든 작그룹에 중앙값이 위치하도록  4-2)의  작그룹max vs 큰그룹min을 비교해보자 >  [127] [45] --> 작은그룹 최대값 vs 큰 그룹 최소값 7 vs 4 -> swap -> [124] [57]이 완성된다.
#    3) 큰그룹에 삽입하면? [12] [457] ->  2 vs 4 no swap -> 그대로 [12] [457] -> but 작그룹에서 중앙값이 나오진 않는다.
#    -> 항상 작그룹에 삽입해서, 작그룹max를 끄집어 내도록 통일하자.
#    * -> 이건 홀수개 경우를 먼저 고려할 때는 생각해낼 수 없지만, [쉬운 짝수개 경우 고려 -> 규칙 -> 홀수개에도 그대로 적용되도록 노력 해보는 것]이다.
import sys
input = sys.stdin.readline

n = int(input())

data = [ int(input()) for _ in range(n)]


# 1. 2개의 힙을 써야 -> 중앙값을 순으로 저장하고 뽑아내는 우선순위큐를 만든다.
import heapq as hq

min_heap = []
max_heap = []

for x in data:

    # 2. 갯수를 먼저 비교해서 맞추는 식으로 채운다. 만약 같다면? 작은그룹-최대힙에 채운다. -> 다르면? 큰 그룹-최소힙 채워서 맞춘다.
    small_len = len(max_heap)
    big_len = len(min_heap)

    if small_len == big_len:
        # 2-1. 갯수가 같다면, 작은그룹에 채우는데, 최대힙이라 -를 달고 넣고 -달고 꺼낸다
        hq.heappush(max_heap, -x )
    else:
        hq.heappush(min_heap, x)

    # 3. 이제 각 그룹의 heappop한 값을 비교한다. 
    # - 만약 아직 안채워졌다면? 비교 없이 넘어가서 정답 출력해야함. -> if 있다면 -> 그것도 늦게채워지는 큰그룹-최소힙이 차있어야 비교가 가능하다.
    # 3-1. 갯수맞춘다고 큰그룹-최소힙에 넣어줬는데, 작은그룹-최대힙보다 작은 경우가 있을 수 있다.
    #      heap(list) [0]으로  heappop으로 꺼내지 않고, 최소값(최대값)을 살펴볼 수 있다. ==peak
    if min_heap and  (-max_heap[0] > min_heap[0]) :
        # 3-2. 만약, swap해야한다면 heappop후 heappush를 해줘야한다.
        #  -> 상대heap을 꺼낸 상태에서 삽입해야하기 때문에.. temp가 필수적이다.
        min_temp, max_temp = -hq.heappop(max_heap) , hq.heappop(min_heap)
        hq.heappush(max_heap, -max_temp)
        hq.heappush(min_heap, min_temp)
    
    # 4. 작은그룹-최대힙을 출력하면 그게 중앙값
    print(-max_heap[0])














# ============시간초과코드.. list + bisect 이용했어도 insert시..?
# 1. 들어온 순서대로 크기순 대로 정렬이 되어야하며 -> 힙heap 자체가 값 (혹은 튜플-앞원소)를 기준으로 이진으로 정렬시키면서 삽입함.
# -> 삽입마다.. insert_index가 달라지므로.. 기준값이 다 달라져야하는데..될까?
# 2. pop시 갯수에 따라 //2 나, //2 -1 가 -> 뽑아내는 기준값이 최소값이 아니므로, tuple에 지정해줘야한다?
# -> 가운데 인덱스가 최소값이 도도록 한번더?
# 3. 순서대로 먼저 나가야한다. -> 우선순위큐(최소힙, key 최소값일수록 먼저나감)


# import heapq as hq
# import bisect
# p_queue = []

# stack = []

# for x in data:
    # if stack:
        
    #     # 들어올 x가 기존queue에서 몇번째에 삽입과 동시에 정렬이 되어야함.
    #     insert_idx = bisect.bisect(stack, x)
    #     stack.insert(insert_idx, x)
        
    #     # 찾은 insert_idx마다 기준값으로 주고.. 

    #     length = len(stack)
    #     if length % 2 !=0:
    #         # 홀수면 //2 idx
    #         print(stack[length//2])
    #     else:
    #         # 짝수면 //2는 오른쪽이니까, 왼쪽꺼 = length -1
    #         print(stack[(length//2 )- 1])
    # else:
    #     # 빈상태면 그냥 넣고 말하면됨
    #     stack.append(x)
    #     print(x)

