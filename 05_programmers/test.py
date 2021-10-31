# 느낀점:
################  ################
# - 가장 맵지 않은 두 음식을 골라야 하므로, sorting은 필수!
# 여기서 중요한 점은 데이터를 저장하고 삭제하는 과정에서 정렬 상태를 유지해야한다는 것입니다. 그럼 섞을 때마다, 정렬을 해주면 되겠군요! 즉, 다음처럼 풀수 있겠지요.
# 데이터 저장/삭제 시 정렬을 유지하는 자료구조를 알고 있습니다. 맞습니다. "힙" 혹은 "우선 순위 큐"
# 아~ 연속해서 뽑아도 <내부에서는 정렬을 유지하는 자료구조>로서 가장 작은 순으로뽑아지도록 해야해서.. heap을 쓰는 구나.. 최소힙..

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
import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    cnt = 0    
    while min(scoville) < K:
        if len(scoville)<2:
            return -1   
        
        low_1, low_2 = hq.heappop(scoville), hq.heappop(scoville)
        if low_2 == 0:
            return -1
        
        hq.heappush(scoville, low_1 + low_2*2)
        cnt+=1
        
    return cnt

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