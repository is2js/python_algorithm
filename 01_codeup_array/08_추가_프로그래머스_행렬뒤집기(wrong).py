
# 느낀점
# - 정처기식은 for i for j -> i>j 행렬의 왼/아래쪽 부분을 잡고 -> swap
# - 새로운 리스트를 만들어놓고 append할거면 -> 새로운 list의 i번째행을 채운다고 치고,for문을 활용한다.
# - *언패킹으로 2차원리스트의 행만 콤마로 꺼내놓고 -> zip으로 각 행들의 i번째 요소를 동시에 가져오면 -> 각 행의 i번째 열값이 모두 모인다.

# 문제
# solution 함수는 이차원 리스트, mylist를 인자로 받습니다
# solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.
# 예를 들어 mylist [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 주어진 경우, solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.

from pprint import pprint
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pprint(mylist)

n_row = len(mylist)
n_col = len(mylist[0])

# 1. 뒤집어졌을 때, 빈 리스트 만들고 -> 빈 리스트의 i행에 채우도록 for문 돌리기
new_list = [[]*n_row for _ in range(n_col)]
print(new_list)

# 1-1. new_list의 i을 append로 채운다 생각하고 mylist를 돌려보자
# for i in range(len(new_list)):
#     new_list[i].append()
# 1-2. i행에는 mylist의  [all]행 [i]열이 다 와야한다. -> 내부에서 for j로 한번더 돌려 mylist-all행을 확보함.
for i in range(len(new_list)):

    for j in range(len(mylist)):
        
        new_list[i].append(mylist[j][i])

print(new_list)


# 2. zip(*2nd_array)
# 1) python의 *사용시언패킹으로 2차원행렬의 행들을 동시에 얻고, 
# 2) zip을 통해, 행들의 각 열 요소들을 동시에 다루자.
# - zip은 각 iterator의 i번재 요소를 동시에 다룰 수 있다. 작은 것위주다.
# - x,y,z in zip() 으로 나누어서 안받을 거면, 각 iter의  i번째 요소들이 1개의 집합을 이룸. -> 행이됨..
print([newrow for newrow in zip(*mylist)])