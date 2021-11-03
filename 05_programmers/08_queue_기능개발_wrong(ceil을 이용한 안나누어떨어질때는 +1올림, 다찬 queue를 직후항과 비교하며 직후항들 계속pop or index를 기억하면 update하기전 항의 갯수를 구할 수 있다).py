import math

# --==============대박2) 조건에 맞는 index를 업데이트함과 동시에, update직전에 현재항index - 직전까지의 index 로 항의 갯수를 구할 수 있다.======================
def solution(progresses, speeds):
    import math
    
    # 1. 나누어떨어지면 그 정수, 그렇지 않으면 올려서 걸린 days list를 구한다.
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    answer = []
    
    # * 2. lst를 돌면서, 나보다 더 큰값이 나올 때, [값이 아닌 index] 저장하도록 update하고 (값 추출이 아닌, 중간지점마다 index 추출후 갯수 구하기가 목적)
    #     update 직전에, [업데이트유발 현재index -  이전index의 차이]로 데이터의 갯수를 계산하는 sense
    # -> my) 특정값  update마다, index를 저장해놓으면, 현재index-저장index로 [값] 뿐만 아니라 [데이터의 갯수]를 알 수 있다!!
    prev_idx = 0 # 중간중간마다 조건만족 index 저장용 -> 그 순간마다 update(저장)전에 현재index - 직전까지의 index로 배열의 갯수 구함.
    ret = []
    for i in range(len(progresses)):
        # 더 큰놈이 나타난 순간.. 업데이트 하기 전에,    
        # prev(그전큰놈)------i더큰놈  사이에 [그전큰놈~ 더큰놈-1]까지의 데이터 갯수를 구한다.
        # 그냥 빼면,, 양쪽 1개만 포함되니 갯수 될듯
        if progresses[prev_idx] < progresses[i]:
            ret.append( i-prev_idx) # 갯수저장
            # 현재항 이용 갯수 구한 뒤, 직전까지 큰놈idx를 업데이트
            prev_idx = i
    
    # 더 큰게 나타났을 때만, [직전~더큰-1까지]  저장 ->  더 큰게 안나타나면  [더큰~n-1끝]까지는 추가 안된다.
    # n-1에서 나타났어도..  prev_idx부터 끝까지. counting되어야하네..
        #if prev_idx != len(progresses)-1: -> 넣으면 안챙김..
    ret.append( len(progresses)-1 - prev_idx  +1 )  #둘다 포함이니 +1

    return ret
# --==============대박1) queue를 이용하여 기준-직후들 조건시까지 pop하면서 비교하여 cnt하기 ======================
def solution(progresses, speeds):
    # 나누어떨어지는 정수 그대로, 남으면 올림을 한번에 
    # // 는 [나누기+floor]라서.. 
    # 직접 [나누기+ceil]로 한줄처리하기
    # finish_days = []
    # for p, s in zip(progresses, speeds):
    #     if not ((100-p) % s):
    #         days = (100-p) //s
    #     else:
    #         days = (100-p) //s +1
    #     finish_days.append(days)
    import math
    f_times = [ math.ceil((100-p)/s) for p,s in zip(progresses, speeds) ]
    #print(f_times)
    #[7, 3, 9]
    
    # 이제, 직전과 비교해서 count만 하면된다.
    # - 직전과 비교해서 pop 및 재배열이 필요하면 stack
    # - 직전과 비교만 할거면 for i, i-1로도 충분?
    # -> 직전과 비교해서 작으면 카운트 누적..
    # -> 커지면,, 새로운데 카운트..
    # ret = []
    # cnt = 1
    # for i in range(1, len(f_times)):
    #     if f_times[i-1] <f_times[i]:
    #         # 기존에 쌓인 것을 새로운 곳에 담아서 cnt 1부터 시작하기
    #         ret.append(cnt)
    #         cnt=1
    #     else:
    #         # 기존 카운트 누적하기
    #         cnt+=1
    # ret.append(cnt)
    # return ret
    
    # queue에 집어넣어놓고, 넣은 순서대로 꺼내면서
    # 뒤에께 <나보다 작은거 나올때가지 계속> 같이 출시될거니 pop + cnt+=1
    # < 앞에서부터 직후꺼와 pop하면서 계속 비교!!> while dq를 쓰는구나.
    # < 뒤에서부터 직전꺼와 pop하면서 계속 비교 -> stack>
    ret_cnt = []
    # 직전꺼가.. 나보다 크면.. 그건.. ?? 비교안된넹..
    # 앞에서부터 -> 뒤를 갈아치우면서 비교해야하네 -> queue
    from collections import deque
    dq = deque(f_times)
    
    # stack이든 queue든 for x in data:로 넣으면서 pop작업하기도 하지만
    # * 이미 들어가있는 것만 pop할 수 있다. -> while dq(stack) + pop기준 비교용 초기항만 빼놓고 시작한다.
    while dq:
        a = dq.popleft()
        same_cnt = 1
        while dq and a >= dq[0] :
            # 작으면 계속 빼제끼면서 cnt한다.
            dq.popleft()
            same_cnt+=1
        # 큐가 비었거나 or 더 큰게 나타난 상황 -> 모아준다. 기준을 바꾸는 것은 담턴에 dq[0]가 새롭게 뽑혀서 a에 자동으로 들어가니 놔둔다.
        # * 더 큰게 나타났을 때, 안빼고, 다음 loop에서a의 기준이 되도록 새로 뽑히도록 한다.
        ret_cnt.append(same_cnt)
        
    # 큐 비었으니.. return해준다?
    return ret_cnt








# --====================테케 2개만 맞고 통과 못함======================
# ==== 직전과 비교해서 재배열?pop?이 아니라.. 갯수cnt라... 굳이 stack할필요없나?
# def solution(progresses, speeds):
#     #from collections import deque
#     #dq = deque([])
#     stack = []
    
#     finish_days = []
#     for p, s in zip(progresses, speeds):
#         if not ((100-p) % s):
#             days = (100-p) //s
#         else:
#             days = (100-p) //s +1
#         finish_days.append(days)
#     print(finish_days)
    
#     cnt=0
#     for day in finish_days:
#         if stack and stack[-1][0] >= day:
#             # cnt업데이트없이 해당 cnt를 넣어줌.
#             stack.append((day,cnt))
#             continue
#         # 직전거보다 크면.. 증가된 cnt를 넣어줌?
#         if not stack:
#             stack.append((day,cnt))
#         elif stack[-1][0] < day:
#             cnt+=1
#             stack.append((day,cnt))
        
        
#     #print(stack)
#     # 이제 각 레벨별로 젤 앞대가리에 있어서 가장 오래걸린 앞작업을 기준으로, 뒤에딸린 완료 작업 갯수까지 같이 출력
#     finish_num= stack[-1][1]
#     last_lst = []
#     for i in range(finish_num+1):
#         k = [ x for x, y in stack if y==i]
#         num = len(k)
#         last_lst.append(num)
            
#     return last_lst