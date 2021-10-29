# =============================
# 느낀점:
# 1. 촌수문제 -> 그래프 중 Tree형태 -> [자식]마다 부모1개값 저장 or [부모]마다 자식들list저장을 확인한다.
# -> Tree의 자식[index]마다 부모[1개값]저장 배열시, default 0으로 range(N+1)로 n도 쓰도록 선언해준다.
# * 2. 자식들의 부모저장배열 만  있으면 -> while x의 부모 p[x]가 존재한다면 계속 -> <재귀적으로 내가 부모가 되도록 update>하여
# 2-1) 나부터, 촌수거리0으로서  (부모, 촌수거리)를 추적해서 모을 수 있다.
# -> 주의: while parents[x] > 0 이어야함. 줄어드는 값도 아닐 뿐더러, 헛개비 p[0]=0에 걸려 무한루프 돌 수도 있다.
# * <무한루프될수도있지만, 첫번째 p[x]=0인 root node x는 넣어줘야한다.> -> while문 돌고나와서  마지막에  한번 해준다.
# -> 시작 값이 들어있는 변수를 초힝값으로 쓰면서, 업데이트해준다.
# -> A: 나 자신으로서 초기값이지만, 업데이트 된다. -> while if절 조건에 사용된다. -> 무한루프, 헛개비 p[0] =0 에 빠지지 않게 조심하자.
# -> Ad: 업데이트되면서 늘려줄 숫자, A의 조상Aa에 같이 쌓일 변수로서 같이 업데이트 된다.
# * 3. 나와 거리를 구하는놈의 [(조상, 거리) 튜플list] 2개list를 <2중for문으로 1:1매칭>시켜 젤 먼저 등장하는 공통조상을 뽑아서 거리륻 더하면 된다.
# * 4. 1:1 매칭시켜 확인시 2가지 방법
# 1) 2중 for문 : 값 or 값의 원소
# 2) for + if in : 값을 비교 : in자리에 comp사용해서 변형하면 값의 원소 추출도 가능
# * 3) for _ if  any( comp)  : 값의 원소를 추출해서 비교가능


# =============================
import sys
sys.stdin = open("./input.txt", "rt")

# =============================
N = int(input())

A, B = map(int, input().split())

# 1. 촌수는 Tree형태 그래프인데, 문제에서 부모(1개만) 저장하는 방식을 택했으니
# -> 1차원 배열에 다가 받아준다. 
# -> 자신의 부모를 모두 0으로 초기화 해놓는다. (1부터 시작하는 node -> 0은 부모가 없다는 것을 표현함.)
# cf) 자식들y는 여러개일 수 있어서  index에 놓고, 각 자식들에 대한 부모는 1명밖이다 -> value로서 1개
p = [0 for _ in range(N+1)]

# 2. 관계수를 for문에서 바로 받아, 각 관계 -> 부모배열을 채운다.
for _ in range(int(input())):
    x, y = map(int, input().split())
    # * 3.우리는 1차원 배열에 [부모만!] 저장한다.
    # 1 2 중에 1이 부모니까 index 2에다가 1를 저장한다.
    # cf) 자식들y는 여러개일 수 있어서  index에 놓고, 각 자식들에 대한 부모는 1명밖이다 -> value로서 1개
    p[y] = x

# 3. A와 B의 공통 조상을 찾기전에,
# * A의 조상들을 모두 모은다, B의 조상들을 모은다 -> 교집합?
# ** 참고로, A조상을 모을 때는, A자신을 포함해서 A자신 정보, 촌수거리0 부터 시작해서 -> 재귀적으로 (부모, 부모까지거리(+=1)의 정보를 호출해서 담는다.
Aa, Ba =[], [] # Aa: A의 조상a, Ba : B의 조상a
# * A의 조상들(부모, 부모의 부모.. ) 모으는 과정에서, A와의 촌수도 같이 튜플로 저장하기 위해
Ad, Bd = 0, 0
# 1) 자신x<-부모p[x]로 업데이트하여, 부모의 부모도 다음번에 찾아가게함
# 2) 자신<-부모 업데이트할 때, 거리도 +1 업데이트해서, 촌수도 올라가게 함.
# 3) p[x] > 0를 while if조건절에 놓아서, p[x]==0 부모가없는 지점까지 올라간다.
while p[A]>0:
    # 3-1) 제일처음에 들어가면, 나와의거리Ad=0인.. 나 자신을 0촌 조상으로 튜플로 넣어준다. (나, 나와의거리)
    Aa.append( (A, Ad))
    # 3-2) 재귀적으로 내가 부모가 되도록 업데이트해서, 
    # while p[updated A]부모의부모가 있다면 -> (나 updated A=부모, 전보단 늘어난 거리updated Ad +1)
    # 을 조상으로서 재귀적으로 모아준다.
    Ad+=1
    A = p[A] # 내가 내 부모가 된다. for 다음단계를 위한 업데이트

# * <무한루프될수도있지만, 첫번째 p[x]=0인 root node x는 넣어줘야한다.>
# * 부모가 없는 p[A]=0의 root node도 넣어줘야한다... root node가 공통조상이 될 확류은 높다.
# - 현재 p[A]==0상태이며, 첫 0이라서.. 루트노드로 업데이트된 것 일 것이다.. 마지막에 한번만 넣어주자.
Aa.append((A, Ad))

# 4. B도 마찬가지다. 
while p[B]>0:
    Ba.append( (B, Bd))
    Bd+=1
    B = p[B] 
Ba.append((B, Bd))


# print(p)
# * 5.  2개배열을, <2중 포문>으로 1:1매칭 해보면서, 튜플 (조상, 촌수) 중 조상이 같을 때를 찾늗나.
# -> 조상이 같은 순간에서 촌수를 더해버리면 된다.
# for i in Aa:
#     for j in Ba:
#         # 여기는 Aa, Ba 조상들의 1:1매칭 공간
#         if i[0] == j[0]:
#             print(i[1]+j[1])
#             # 등장하면, 제일 빠른 것을 만난 순간 바로 프로그램을 종료하면 된다.
#             exit()
# else:
#     print(-1)

# 1:1매칭을 변환없이 확인 -> for + if in
# 1:1매칭인데 인덱싱들 해서 확인 -> for + if any( x , y indexing  for y in comp)

