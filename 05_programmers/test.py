# * 느낀점:
# * 1. if not 배열 or 배열조건: 배열이 비었거나 or 차있더라도.. (길이가 1이상..)조건이 있으면~
    # * 원래 arr or -1 : arr 차잇거나 or None으로 비었으면 -1을 default값으로 넣기
    # * 응용 25번 / 프로그래머스07번 -> if not arr[k]  or  arr[k] == ???: 
    # ** --> k번째 배열이 비었거나 혹은 차있어도 ??면..
    # cf) if not k%n -> 0이면 == k가 n의 배수이면,, (1이상 들어오게했을 때) 
    # cf) if not arr -> 배열이비었으면 == arr이 비었으면
    # cf) if not arr[k] -> 배열 arr[k]가 비었으면
    # cf) if not arr[k] or arr[k] == ?? -> 배열arr[k]가 비었거나, < 차있더라도  ???면>
# * 2. 문자열 그래프를 dict hashmap으로 저장한다. DFS은 부모-자식list가 있으며 안끊기고, 돌아와서, 잘 탐색한다.
# -> 만약, DFS-stack을 쓰지 않으면, 종착역에서 빽/돌아감 없이 끊겨버린다.
# --> DFS를 쓰면, 부모-여러자식에서, 연결이 더이상 안되면, 빽 한 뒤에, 같은부모-다른자식을 빼서 탐색한다.
# * 1) defaultdict로 부모key-자식들list를 모아넣는다.
# * 2) 자식list마다, 탐색 우선순위를 정렬로 만들어준다. -> <우선순위 높을 수록 뒤에 역순으로 배치> -> pop으로 꺼내오기 
# * 3) stack = ['ICT']에는 일단 시작좌표를 넣어놓고 시작한다. path = [] 는 종착역들을 모아놓을 좌표로, 마지막엔 시작좌표까지 모인다.
# * - path는 맨 마지막에 시작좌표가 들어오므로, 출력시 역순으로 출력해야한다. path[::-1]
# * 4) DFS는 while stack으로 돌면서 ->  stack[-1]의 top이 <부모노드>로서 2가지 경우의 수를 가지게 한다.
# * 4-1) dict의 key(부모)로 등록안됬거나 (if top not in dict)  or key(부모)로 등록됬더라도, 자식이 더이상 없는 경우 [] ( or not dict[top])
# *      부모가 아닌 [종착역]으로서,  1) stack에서 pop -> 2) path에 등록   
# *      즉, stack[-1]이 종착역으로 조회되면, stack에서 pop, 종착역모음에 append  
# ***    my) stack에는 종착역은 없다! 자식 가진 node들만 들어갔따가, 자식 다떨어지면 종착역으로 나온다!
#        my) dict의 key조회시 쓰면 먼저 key있는지부터 검사하도록 or로 하면 좋겠네!   if key not in dict or  dict[key] 조건 
# * 4-2) dict의 key(부모)로서, 자식을 가져, 1) 자식list pop  2) stack에 등록
# ***    my)  stack에는 자식가진 node들만 들어가서, 자식들 탐색한다. 자식 없으면, pop, 종착역으로 !
# * 5) path에 모인 모든 종착역들을.. 좌우반전해서 출력

# * 3. 종착역을 저장만 해두면, 끊기지 않고 연결되나??

# * 우선순위 높은 자식이라도, stack에 등록되었다가... 종착역으로 판명되면.. path로 들어갈 듯? 
# * stack은 자식을 가진놈들이 자식의 자식 또한 쌓일 것이다. pop은 더이상 자식이 없을때마다 하나씩빠진다.
# * 그렇다면.. 자식 없는애들이 path에 쌓일건데, 역순으로 출력하더라도... 연결이 되나?
# ** <우선순위자식>이 자식없어 종착역 등록 -> stack에는 [종착역의 부모]가 <그다음 우선순위 자식>을 탐색 중 -> 없으면 바로 [빽, 직전, 종착역의 부모node]가 종착역이 되는 것이 DFS의 stack 개념
# *** 그다음 우선순위 자식은.. 무조건 길이 있다(다 탐색해야하니) -> path [1st, ]  stack[부모, 2nd, 2nd자식..] -> 이상황에서 다 연결되나?
# https://deok2kim.tistory.com/118
# *** 종착역을 버리지 않고, path에 stack처럼 저장만 해두면, 
# *** 마지막 stack의 길이 끝나는 순간, path에 등록만 해두면 알아서, 끝까지 연결되는 것 처럼된다.
# [ICD,A]  [A,B]  [A,C]  [C,A]  [B,D]  가있다고 치자.
# 
# ICD -> A -> B -> D : 끊겨서 종착역 -> path에 [D, B 저장]
#          
#   [A,C]  [C,A] 만 남음
# 
#           C -> A : 2) 끊겨서 종착역에 넣으면 ------------------>  [D, B, A, C, A, ICD]
#         /
# ICD -> A -> B -> D : 1) 끊겨서 종착역 -> path에 [D, B]
# 
# * 결론: 마치... 종착역일떄마다 path에 담아두기만 하면서, 자식들을 탐색하면, 알아서 이어진다.
# -> 한붓그리기도 이런 원리?






# =================재귀: 왜 종착역이 if ==N+1: 인지 이해가 안되서 일단 보류=========================
from collections import defaultdict 

def dfs(graph, N, key, footprint):
    print(footprint, len(footprint))
    if len(footprint) == N +1:
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country)

        if ret:
            return ret


def solution(tickets):
    answer = []

    graph = defaultdict(list)

    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer









# ===========================================
def solution(tickets):
    # 0. 힙으로 최소값만 꺼내면서 dict에서 꺼내면서 연결하는 경우 -> 끊긴 node를 만났을 때 종료되어버린다.
    #    DFS-stack을 활용한 직전node를 알아야, 끊어질 경우 돌아올 수 있다!!
    
    # 1. 재귀없이 lst_stack을 활용해서, 끊길때 빽할 정보 저장하면서 DFS 전수조사 하기
    
    # 1) 그래프가 숫자면 1부터 인접행렬or인접리스트를 그리는데, 
    #    문자열이므로, dict로 인접리스트를 생성한다.
    from collections import defaultdict
    routes = defaultdict(list)
    for st, ed in tickets:
        routes[st] += [ed]
        
    # 2) 각 ed지점(자식node) list를  우선순위 높은 것들이 뒤에오도록 <역순으로 정렬>해놓음 -> pop이 먼저 나오니까.
    # - hashmap(dict)에서 꺼낼 자식node list도 stack(역순정렬해놓고 먼저꺼내는 용도의stack),  & 현재 진행node = 빽할 node도 stack(직전꺼 나와야함)
    # - 진행중인 node의 자식이 []비었을 경우.. -> 종료..? 
    # - 종료되었으면.. stack에 쌓인 순서대로  빽해서 빠져나와야함..
    # -> 그걸 또.. path에 저장 ... path에서는 빽한ㄴ순서 젤 먼쪽부터? 
    # -> path를 가까운순부터 꺼내기 -> 뒤에서부터 꺼내기 -> pop으로 하나하나 X 슬라이싱으로 stack한벙네 pop하기
    
    # 3) DFS로직
    # 문제 조건에 따라, "ICN"을 스택에 먼저 넣습니다.
    # 스택이 빌때까지 다음을 반복합니다.
    # 스택에서 가장 위의 저장된 데이터 top을 꺼내옵니다.
    # 만약 top이 그래프에 없거나, top을 시작점으로 하는 티켓이 없는 경우, 스택에서 꺼내와 path에 저장합니다.
    # 2번이 아니라면, top을 시작점으로 하는 끝점 중 가장 마지막 지점을 꺼내와 스택에 저장합니다.
    
    # 탐색시 자식list중 맨 뒤에것부터 쓸 건데, 문제요구사항대로 우선순위높은 것을 맨 뒤로 준다.
    for st in routes.keys():
        routes[st].sort(reverse=True) # 모든 자식list 역순정렬  NlgN 
    
    # ==DFS by stack직접 사용==
    stack = ['ICN'] # 최초는 넣어주고 진행node라고 가정한다. -> 종착역(부모로 등록X or 부모등록인데 자식들이 종착역으로서 다 빠져나감.)
    path = [] # 자식이 없는 종착역들을 등록한다. 
    
    # stack은 pop을 활용할거고, append도 해줄것이다. 이것으로 종착역시 처리->돌아가며 전수조사한다?
    while stack:
        top = stack[-1] # 안꺼낸다. 초기 시작좌표 1개 있던 거 꺼내고 안넣으면 바로 종료되서? pop조건확인시에도 잘 안꺼내고 [-1]로만 확인한다.

        # [1] 진행중인 top node가, routes dict (부모->자식리스트 dict)에서 
        # 1) 아예 시작점(부모)으로 등록도 안됬거나(등록X)
        # 2) or 시작점(부모) 등록은 됬더라도 -> 이미 자식은 탐색되어, 갈수 있는 list가 비어있다면? 
        # --> 종착역으로서,  stack에서 제거함으로써 빽하여, 직전노드 진행상황으로 돌아가고, 종착역은 path에다가 모아준다.
        if top not in routes or (not routes[top]):
            # 종착역은 <stack에서 pop한 뒤> path에 등록해준다.
            path.append(stack.pop())

        # [2] 진행중인 top node가, routes dict에 자식리스트가 1개이상 존재한다면
        else:
            # 자식 list 중에 제일 우선순위 높은 놈[-1]을 가져와 <stack에 등록> 해준다.
            # * 우선순위 높은 자식이라도, stack에 등록되었다가... 종착역으로 판명되면.. path로 들어갈 듯? 
            # * stack은 자식을 가진놈들이 자식의 자식 또한 쌓일 것이다. pop은 더이상 자식이 없을때마다 하나씩빠진다.
            # * 그렇다면.. 자식 없는애들이 path에 쌓일건데, 역순으로 출력하더라도... 연결이 되나?
            # ** <우선순위자식>이 자식없어 종착역 등록 -> stack에는 [종착역의 부모]가 <그다음 우선순위 자식>을 탐색 중 -> 없으면 바로 [빽, 직전, 종착역의 부모node]가 종착역이 되는 것이 DFS의 stack 개념
            # *** 그다음 우선순위 자식은.. 무조건 길이 있다(다 탐색해야하니) -> path [1st, ]  stack[부모, 2nd, 2nd자식..] 
            # https://deok2kim.tistory.com/118
            # *** 종착역을 버리지 않고, path에 stack처럼 저장만 해두면, 
            # *** 마지막 stack의 길이 끝나는 순간, path에 등록만 해두면 알아서, 끝까지 연결되는 것 처럼된다.
            # 

            stack.append(routes[top].pop())
            # pop했다 치고, 자식들 중 맨 뒤에 한개를 빼준다.
            #routes[top] = routes[top][:-1]
    
        #print(path, stack)
    
    # 종착역을 모은path를 거꾸로 출력해준다.
    # - pop하면서 [부모로서 등록안된 or 자식없는(사용해서 더이상 없는) ] 종착역들을 모아갔으니, 맨끝에서부터 착착 들어올 것이다. 이 때, 우선순위를 미리 정해서 탐색했으니.. 원하는 순서대로 모았을 것이다?
    answer = path[::-1]
    return answer

# 입력값 〉	[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# 기댓값 〉	["ICN", "JFK", "HND", "IAD"]
# 실행 결과 〉	테스트를 통과하였습니다.
# 출력 〉	
# stack:['ICN', 'JFK'] 
#  path:[]
# stack:['ICN', 'JFK', 'HND'] 
#  path:[]
# stack:['ICN', 'JFK', 'HND', 'IAD'] 
#  path:[]
# stack:['ICN', 'JFK', 'HND'] 
#  path:['IAD']
# stack:['ICN', 'JFK'] 
#  path:['IAD', 'HND']
# stack:['ICN'] 
#  path:['IAD', 'HND', 'JFK']
# stack:[] 
#  path:['IAD', 'HND', 'JFK', 'ICN']
# 테스트 2
# 입력값 〉	[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
# 기댓값 〉	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
# 실행 결과 〉	테스트를 통과하였습니다.
# 출력 〉	stack:['ICN', 'ATL'] 
#  path:[]
# stack:['ICN', 'ATL', 'ICN'] 
#  path:[]
# stack:['ICN', 'ATL', 'ICN', 'SFO'] 
#  path:[]
# stack:['ICN', 'ATL', 'ICN', 'SFO', 'ATL'] 
#  path:[]
# stack:['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO'] 
#  path:[]
# stack:['ICN', 'ATL', 'ICN', 'SFO', 'ATL'] 
#  path:['SFO']
# stack:['ICN', 'ATL', 'ICN', 'SFO'] 
#  path:['SFO', 'ATL']
# stack:['ICN', 'ATL', 'ICN'] 
#  path:['SFO', 'ATL', 'SFO']
# stack:['ICN', 'ATL'] 
#  path:['SFO', 'ATL', 'SFO', 'ICN']
# stack:['ICN'] 
#  path:['SFO', 'ATL', 'SFO', 'ICN', 'ATL']
# stack:[] 
#  path:['SFO', 'ATL', 'SFO', 'ICN', 'ATL', 'ICN']











    
    
# ======dict로 구현해본 내코드=== 테케 다 통과못함.=========
#     from collections import defaultdict
#     import heapq as hq
    
#     p_dict = defaultdict(list)
#     for a, b in tickets:
#         hq.heappush(p_dict[a], b)
#     print(p_dict)
#     sons = []
#     st = 'ICN'
#     while p_dict[st]:
#         if not sons:
#             sons.append(st)
#         st = hq.heappop(p_dict[st])
#         # 꺼낸 값이 p_dict의key로 없으면.. 연결안되고 끊어져버린다.
#         tmp = []
#         while st not in p_dict:
#             tmp.append(st)
#             st = hq.heappop(p_dict[st])
            
#         while tmp:
            
        
            
#         sons.append(st)
#     print(sons)
#     print(p_dict)
    