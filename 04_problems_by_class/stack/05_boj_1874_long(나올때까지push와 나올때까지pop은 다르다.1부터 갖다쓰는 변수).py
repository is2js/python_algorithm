# 느낀점:
#   1. target들을 INPUT창에 따로 뿌려줘도, 미리 배열에 받아두자. [int(input()) for _ in range(n)]
# * 2. [1부터 n]까지를 갖다쓰는데, queue에서 popleft()로 빼 쓸거 아니면 -> <cnt=1부터 갖다쓰는 변수, 쓸때마다 cnt+=1> 작전을 쓰자.
# * 3. target 및 현재수(cnt)에 따라  
# * 3-1) target <= cnt <나올때까지push> : <equal은 push에서 단다!!> 
# * 3-2) cnt < target  <나올때까지pop>  : whjle stack and <no equal의 pop조건>은 [equal전에, 중간에 비었는지 검사를 하여, 알아서 예외처리 된다.]
# * 4. <나올때까지pop>은 중간에 stack비게 되면 -> while후에 [원하는조건직전]에 [not stack]으로 비는지 확인을 하며 [알아서 못찾으면 종료]가 명확함.
# * 5. <나올때까지push>는 stack[-1]이 아니라, 넣기전의 변수(여기선cnt)로 while문을 짜며, equal이 될때까지[원하는 조건까지] push한다.
#  -> 중간에 다른 이유로 멈출일이 없기 때문. <<< 만약, 간격이 +1이 아니고 크면 넘어가버릴 수도 >>>
# *    <나올떄까지push>는 원하는조건직전에 검사할 필요가 없으니, while cnt <= target 처럼, 다 완성되게 조건문을 건다.
#  -> <나올대까지push>는 원하는값 equal조건도 적으며, <pop>보다 위쪽에 적으며, [pop가기전에 else:]로 while조건속 if의 반대경우로 <나올때까지pop>으로 넘어간다.


################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### 백준용
### import sys
### input = sys.stdin.readline
# 단계별로 푸시는 분: https://developer-ellen.tistory.com/33 # 고민 많이 하시는 분이라 챙겨놓음.
######################################################
import sys

n = int(input())

# https://developer-ellen.tistory.com/33
# https://ywtechit.tistory.com/193

# 12. <나올때까지pop while stack and stack[-1] != target >은  pop지점이 stack내 보장 and stack이 대부분 살아있어서 stack[-1]이 보장, 안되는 경우 if not stack:로 빈 스택시 break종료되는 명확한 경우에만 쓴다.
# * 여기서는 <if not stack: 스택이 비면 continue(넘어가기) 혹은 (게임종료)>가 아니기 때문에 --> stack[-1]이 에러뜨는 경우가 많다.
# * stack[-1]이 아니라 <stack에 들어가기전 변수인 cnt>로 판단한다.
targets = [int(input()) for _ in range(n)]
stack, cnt, res = [], 1, ''

for target in targets:
    # 13. stack[-1]을 비교하는 것이 아니므로, stack.pop을 무조건 먼저하는경우가 아니므로 stack이 조건에 들어가지 않는다.
    # -> push하면서 함. 넣기전에 비교함..
    # 1) target > cnt라서  < 나올떄까지 push>
    while cnt <= target:
        stack.append(cnt)
        cnt+=1
        res += '+'
        # cnt == target 같아지는 순간임. push넣고 pop해야함.
    # * 만약 cnt가 target을 넘어선 상황이 오더라도, append는 안일어남.
    # while은 if와 같아서 약간 배반의 상황이라고 하면, 애초에 진입을 안한다. 따로 위쪽while과 아래쪽 while을 if / if로 보고 각각에서break할일 없다.
    # 하지만..ㅠㅠ while pop 조건끝나고의 문장에 걸리네.. -> else
    
        
    else:
        # 2) 나올때까지 pop -> stack조건이 들어감. cnt는 
        while stack and stack[-1] != target:
            stack.pop()
            res += '-'
        # 2-2) 같아지기도 전에 먼저 고갈되면 종료
        if not stack:
            print("NO>>", stack)
            break 
        # 같아지는 순간임2.
        stack.pop()
        res += '-'

else:
    print(res)
    print("다 통과")

# 14.
# 12534는 다 걸러질까?
# 1 -> 2 ->  345 -> 34 -> 3 -> ?
# 4가 이미 <나올때까지pop>되버렸고, <1부터갖다쓰는 변수>는 이미 6을 바라보고 있음
# -> 4는 이제 나올수가없다. -> <나올때까지push>의 전제조건이 while cnt <= target이므로
#  cnt 6 <= 4 으로.. cnt가 증가도 안되고 while문 들어가지도 못함.
# -> 나올때까지 push를 안타고.. 나올때까지  pop인데.. 
# -> <나올때까지 pop>은.. pop 끝까지하다가 while stack and [원하는조건]을 충족전에 if not stack되면 종료되는 것을 전제로하니
# -> 종료되버린다.




# # 0. target숫자가 <나올때까지 pop>하는 로직이 있으므로 stack을 쓰는데, 여기선 <나올때까지 push>도 있다.
# # 1. target들을 따로 뿌려줘도, 미리 배열로 받아두기
# targets = [int(input()) for _ in range(n)]
# # 2. target까지 오름차순으로 <순서기억> stack에 쌓다가 k=pop으로 풀어놓음. target 만날 시에도 pop -> stack 사용
# stack = []
# # 3. <1부터 증가되면서 하나씩 사용>하는데, 자료구조이용해서 <1부터 순서대로> 하나씩 빼쓰는 <선입선출?queue?> 대신 <내려가지 않는 cnt +=1 변수>를 사용할 수 있다.
# cnt = 1 
# 4. 기존) stack에 들어있는 target(짝원소-시작원소)만날때까지 pop
#    현재) 첫번째에는, target에 대해, 1부터 target까지 push후, pop 1,2,3,[4] -> 1,2,3 
#  * 근데) 2번째부터는, target이 stack[-1]보다 <같거나> 바로pop(조건에 걸려서 동일?) <크면> push후 pop(동일) ---> <같을때까지 push후> while stack and stack[-1] != target: stack.pop() 
#  *      target이 stack[-1]보다 작은 경우,   1,[2],3 -> 3 pop -> 1 [2] -> 1                         ---> <같아질때까지 pop>
#  * 문제) cnt는 push할때마다 < 따른데서 1부터 빼쓰는 중 >이라 +=1 커질수밖에 없음. -> stack 1 상태에서


# #  5. 첫번째가 push만 무조건할 수 있다면, 초기항으로서 쉽게가자!! -> if조건에 stack[-1]을 사용할 수 있음. 없으면 .. 만들다가 stack빈 거라서 이제.. 끝난거?
# # -> 일반화 안되나?
# for target in targets:
#     # 6. target과 stack의 수를 비교해야한다. 근데 첨엔 stack이 있으니.... stack을 채우는 경우의수부터 앞에 줘서 한다?
#     # * [while 나올때까지 pop]  <  [while 같아질때까지 push]: 편의상 먼저한다! 어차피  while if조건문에 걸려서 while 타지도 못한다.
#     # 7. [while 같아질때까지 push]는  stack길이조건 제한이 없다! (원형아니면)
#     # * -> 나올때까지 push도.. 일단 stack[-1]로 비교를 해야해서ㅜㅜ 일단 채워지는 조건부터 한다.
#     # * -> 최초라는 조건을 cnt ==1 로 만들어서 push하면될듯하다. + 첫 타겟은 push로 채우고 시작하자.
#     if (cnt == 1) and (not stack):
#         while cnt <= target :
#             stack.append(cnt)
#             cnt+=1
#     # 9. 나올때까지 push는 넣는 조건이라 좀 더 위에 주자.
#     # - 근데 stack[-1]이라서.. stack이 비어있으면 안된다.
#     if target >= stack[-1]:
#         while stack[-1] != target:
#             stack.append(cnt)
#             cnt+=1
#         # 만난 순간
#         stack.pop()
#         # 통과
    
#     # 8. 조건에 따라, 나올때까지 push  vs  나올때까지 pop
#     # 나올때까지pop
#     if stack and target < stack[-1]:
#         while stack and stack[-1] != target:
#             stack.pop()
#         # 중도탈락
#         if not stack:
#             print("NO")
#             break
#         # 통과


#     # 10. 돌고 있는데 stack이 빈 경우??
    
#     # 11. 문제는 target이 term이 있어서, 만나서pop이 아닌, <중간에 나올때까지 pop>으로 날아가버린 수를 target이 나오면 찾아갈 수 가 없다.
#     # -> 못찾는 상태에서 무한정 같아질때까지 push를 할 수도 있다.

#     print(stack)
    

        




# =================내 정답코드 =====================
# stack = []
# i=1
# result = ''
# for _ in range(n):
#     k = int(input())
        
#     # 1. 일단, 1~n사이의 숫자가 있으며, k까지는 stack에 집어넣어야한다.
#     if not stack :
#         stack.append(i)
#         result +='+'
#         i+=1

#     if stack and stack[-1] < k:
#         # 추가... k가 더 큰데, 추가할 i가 더 큰 상태라 추가할 수없는 상황(이미 추가해서 pop)
#         if i > k :
#             result = "NO"
#             break

#         while stack[-1] != k:
#             stack.append(i)
#             i+=1
#             result +='+'

#     elif stack and stack[-1] > k:
#         while stack and stack[-1] != k:
#             stack.pop()
#             result +='-'
    
#     # 어떻게든 같아진 상황
#     # -> 같아질려다가 pop으로 인해 고갈되어서 더이상 pop못함 -> k못꺼냄.
#     if not stack:
#         # print("NO")
#         result = "NO"
#         break
#     else:
#         # print(stack.pop())
#         stack.pop()
#         result +='-'
#     # print("result :>>", result)

# print(result)

# # if result == "NO":
# #     print(result)
# # else:
# #     for x in result:
# #         print(x)
            






