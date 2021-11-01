# 느낀점:
################  ################
# * 1. N을 k번 사용 만들어진 결과물 중에 number가 있는지 확인해서 발견 -> 1~ 8번 결과물set까지 확인한다. 
# -> 1번만에 만든 것들을 set에 add / ~ 최대 8번만에 만든 것들을 set에 add하도록, 
# * <중복이 어마어마할> 연산결과물 배열을 빈set list로 만든다. [ set() for _ in range(8) ] -> 돌면서   set_lst[i].add() 
# --> 2차원부터는 밖에서 *가 안되며, set()은 안에서 *가 안되니 list comp로 만든다.
# * 2. [0부터 인덱스 & 값 동시 필요] 이외에, [배열값을 돌면서 + 1부터 숫자가 필요할 때]도 enumerate( , start =1 )을 활용한다.
# * 3. 숫자를 연속해서붙이려면 str(N) * k  -> int() 로 변환.
# * 4. 1차원배열인데도 2중반복문을 쓰는 경우? -> 바깥에서 i고정 ->  [고정된 i까지 or 고정된 i이후로 를 탐색]하기 위해서
# * ->  바깥i를 0이 아닌 1부터 진행시키야, j의 탐색은 range(i)만으로 -> 0부터 i-1까지 탐색한다. (range(0)은 없다?)
# ** --> for i range(1, len(arr))  -> for j in range(i)
# ---> 만약, 바깥 i가 그냥 0부터 출발한다? -> j는 range(i+1, ~) 으로 뒤족을 탐색할 예정. or  range(i, ~)로 i부터 탐색할 예정. 그전까지는 없다.
# * 5. 1차원배열 속 모든 값을 -> 1:1매칭시켜 만나기 위해서는, 2중반복문이 사용된다.
# -> for x in s1_arr:  for j in s2_arr:   ->  s1_arr[i] + s2_arr[j]
# ** i고정, 0~i-1까지 j에 대해서,   각 s[j]에 들어간 모든원소 와  s[i-j-1]의 모든 원소를 1:1매칭 시켜 연산한다면?
# for i in range(1, len(set_lst)):
#     for j in range(i):
#         for op1 in set_lst[j]:
#             for op2 in set_lst[i-j-1]:
#                 set_lst[i].add(op1 + op2)




def solution(N, number):
       
    # set1 : N을 1번만 사용하고 number에 도전할 때 필요한 원소들
    # set2 : N을 2번만 사용하고 number에 도전할 때 필요한 원소들
    # set8 : 최대 N을 8번 사용하고 number에 도전할 때 필요한 원소들
    #  8개의 빈 set을 lst를 만들어놓는다.
    set_lst = [set() for _ in range(8) ] 
    
    # 배열속 각 set에 접근해서 add해주면 들어가지낟.
    # 배열을 1개씩 돌 때, index가 아니더라도 1부터 숫자가 필요하면 enumerate( , start=1)을 활용한다.
    for i, set_ in enumerate(set_lst, start=1):
        # 숫자N을 연달아서 붙혀 생성할 땐 str(N) * k를 이용해서 연달아 붙이고 int()로 숫자를 만든다.
        continueous_num = int(str(N)*i)
        
        # 만약, 정답number가 연달아붙인 것 과 같다면?, N을 i번 쓴게 최소횟수일 것이다.
        if continueous_num == number:
            return i
        set_.add( continueous_num )
    
    # 이제 set_lst를 돌면서 점점 채워나가야한다.
    # -> i+1번 N사용으로 나온 계산결과 --로-->  i+2번 N사용 계산결과 채우기
    
    # 1차원 배열에서 2중반복문으로  바깥for index를 고정 ->  안쪽for 그 index활용해서 안으로 밖으로 움직이기 -> j를 0부터 range(i) or range(i+1, 끝)
    # -> 밖에서 range를 1부터 끝까지.. j는 0부터 i-1까지 range(i)로 나아갈 수 있다.
    for i in range(1, len(set_lst)):
        # 한칸 뒤에서 출발하여, 고정된 i(1, 2, ... )에 대해 -> 0, 0~1, .. 0~끝 까지 움직이면서, 고정된 i보다는 작은 index들 모두를 사용한다.
        for j in range(i):
            # j는 0부터 i-1까지 set_lst의 index에 접근해 원소들을 다 가져온다. -> 1:1 매칭 시키기 위해 2중 포문으로 만난다.
            for op1 in set_lst[j]:
                # 매 작은 것에 접근한 상태에서,  j번사용(j)----[i] = i번 N사용
                # 이제 k = i-j번 사용한 것을 뽑아와야하는데, 
                # 머리속 (i+1)-(j+1)번 사용했다? -> index는 i-j -1 인덱스를 가져와야함.
                for op2 in set_lst[i-j-1]:
                    # s[j]에 있는 모든 j+1번 N사용 경우의수들 마다
                    # 모든 i-j-1 + 1번 N사용 경우의수를 다시 연산해야한다.
                    # 연달아서 붙이는 것은 미리 넣어놨음.
                    set_lst[i].add(op1 + op2)
                    set_lst[i].add(op1 - op2)
                    set_lst[i].add(op1 * op2)
                    if op2 != 0:
                        set_lst[i].add(op1 // op2)
                        
        # 매 i+1번만에 답이 나왔는지 확인해서, 나왔으면 종료시킨다.
        if number in set_lst[i]:
            return i+1
        
    
    return -1