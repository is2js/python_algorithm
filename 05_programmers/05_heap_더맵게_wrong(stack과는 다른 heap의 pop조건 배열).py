# 느낀점:
# * 1. 배열내에서 최소값 최대값 등 가장~ 한 것을 뽑을 때, [2개이상 연속해서 뽑아야한다면], 삽입/삭제시 sort유지 자료구조 heap을 고려하자.
# ** -> <데이터 push/pop> 시 정렬을 유지하는 자료구조 -> heap
# * 2. 이 문제에서 일반 list로 계산시, -> 가장 작은 것 뽑기 N, 2번째도 N-1개 다 살피기 -> 계산에서 -> 가장 작은 자리 넣기 N -> n개를 반복 -> N*N
# ** heap은 매번 lgN으로 넣기/뽑기함. -> N개 * lgN
# * 3. [heap의 pop조건]을 stack과 다르게  조건을 줘야한다.
# ** 3-1) pop전에 while stack 담에 and stack[-1]의 peek보고 주는 조건을 ----> heap에서는 주지못한다. 
# ** 3-2) while hp 먼저 --> min = heappop() 해서 heap[-1]값을 뽑아 -> if 조건을 내부에 하나 더 주는데, 
# ***    [while 도는 조건, 직전까지]  대신, [if while 탈출조건]으로 조건을 건다.
# * 4. 2개 연속뽑더라도, pop전에 heap 비어있지 않은지 조건을 매번 달아줘야한다. 비어있으면 에러 종료
# while scoville: # 4-1) [-1]을 빼올 수가 없어 while에서 추가  도는 조건으로 못줌.
#     first = hq.heappop(scoville) # 4-2) 내부에서 직접뽑아쓰면서, 탈출조건으로 줘야함.
#     if first>=K:
#         break
#     if not scoville: # 4-3) 연속에서 뽑아야한다면, pop전에 비지 않았는지 누적해서 검색해야함.
#         return -1
#     second = hq.heappop(scoville)
#     hq.heappush(scoville, first + second*2)
#     answer+=1
# ###############  ################

# 해설 모음)
# 가장 맵지 않은 두 음식을 골라야 하므로, sorting은 필수!
# 여기서 중요한 점은 데이터를 저장하고 삭제하는 과정에서 정렬 상태를 유지해야한다는 것입니다. 그럼 섞을 때마다, 정렬을 해주면 되겠군요! 즉, 다음처럼 풀수 있겠지요.
# 데이터 저장/삭제 시 정렬을 유지하는 자료구조를 알고 있습니다. 맞습니다. "힙" 혹은 "우선 순위 큐"

# 최악의 경우 :수가 하나 남을 때까지 섞어야 하는 경우(n-1회)
# if 리스트: 정렬된 리스트에 순서 맞추어 원소 삽입 O(n)
# 전체 문제 풀이의 복잡도: n번의 단계를 거치는데 각 단계에서 n에 비례하는 계산을 하기 때문에 O(n^2)

# 힙 구성(heapify) : O(NlogN), 빈 힙에 n개의 원소를 차례로 삽입하기 때문에. 하나의 원소를 삽입하는데 logN만큼 걸리므로 N개의 원소를 다 삽입하면 NlogN




# 아~ 연속해서 뽑아도 가장 작은 순으로뽑아지도록 해야해서.. heap을 쓰는 구나.. 최소힙..
import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0    

    # heap도 stack처럼 pop하기전에 데이터가 있는지부터
    while scoville:
        # and scoville [-1]을 하고 싶지만, stack = lst와 다르게 peek를 볼 순 없으니
        # 내부에서 일단 뽑아서 참고한다(조건에 뽑지X)
        first = hq.heappop(scoville)
        
        # stack이라면 while문에 [반대로, 직전까지] 넣었어야할 도는 조건( while first < K:)을 -> 반대로 <탈출조건>으로 건다. 
        # stack은 탈출조건 대신 도는 조건을 while문에 기입했찌만, heap은 내부에서 if탈출조건을 꼭 명시하자~!
        if first>=K:
            break
            
        # 2번째 원소도 pop해야하니 또한번 검사한다.
        if not scoville:
            return -1
        second = hq.heappop(scoville)
        
        # 합쳐서 넣고 cnt+1
        hq.heappush(scoville, first + second*2)
        answer+=1
        
    return answer






# 힙의 저장과 삭제 연산은 O(log(N))의 시간 복잡도를 가집니다. 또한, 문제에서 최악의 경우, scoville 길이 N만큼 반복하기 때문에, 위 알고리즘의 시간 복잡도는 O(N * log(N))입니다. 실제 코드를 제출하면 정확성 테스트까지 모두 통과하는 것을 확인


# ==========효율성 미통과 코드===============
# import heapq as hq

# def solution(scoville, K):
#     hq.heapify(scoville)
#     cnt = 0    
#     while min(scoville) < K:
#         if len(scoville)<2:
#             return -1   
        
#         low_1, low_2 = hq.heappop(scoville), hq.heappop(scoville)
#         if low_2 == 0:
#             return -1
        
#         hq.heappush(scoville, low_1 + low_2*2)
#         cnt+=1
        
#     return cnt