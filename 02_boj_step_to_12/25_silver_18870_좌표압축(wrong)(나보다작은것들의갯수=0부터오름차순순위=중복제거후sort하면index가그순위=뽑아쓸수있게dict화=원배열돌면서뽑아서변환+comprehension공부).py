"""
author : ChoJaeSeong
github : https://github.com/is2js
e-mail : tingstyle1

title : 좌표 압축
description : 정렬
"""
# 느낀점 : 시간초과는 공간복잡도를 늘리자.(변수사용)
# - 
# 시간초과코드지만, list comp로도 2중for문을 돌릴 수 있다.
# 참고블로그 : https://velog.io/@cosmos/BOJ%EB%B0%B1%EC%A4%80-18870-python
# **- x고정을 원한다면, 콤마로붙어지는 앞쪽의 괄호안에서 돌리기 [  (x를 고정시킨 상태에서, 여기서 for y in data ) for x in data ]**
# - x고정이 아니라, 모든 경우의수를 콤마로 펼칠려면, 뒤에서 한번 더 돌리기 [ for x in data for y in data]

# 좌표 압축을 적용: Xi를 좌표 압축한 결과 X'i의 값은 
# **Xi > Xj를 만족하는 서로 다른 좌표의 개수**
# **my) list에서 나보다 작은 것들의 갯수 == 하나도없으면 0, 1개 있으면 1, ... 0부터 시작되는 i번째 낮은수
# **my) 오름차순 정렬(작은것부터 시작) 시 index(0부터 시작)가 <나보다 작은 것들의 갯수> 동일해짐.**
# 해설: https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj18870/
# 문제에서 원하는 것은, 해당 값이 
# **전체 집합에서 몇 번째로 낮은 숫자인지를 반환하는 것입니다.**
# 이때, 순위를 내려면 정렬을 해서 조사를 하면 되는데, 문제는 중복이 있을 수도 있다는 점입니다.
# 보통이라면 중복이 나오면 넘기고 순위를 다시 매기는 루틴이 필요하겠지만, 파이썬은 set 자료구조를 기본적으로 지원해줍니다.
# 중복을 모두 없앤 후에, 또 기본적으로 지원해주는 정렬 함수를 이용해줍시다.
# 이제 정렬된 리스트에서 각 요소가 리스트의 몇 번째 요소인지 태그를 다는 작업을 딕셔너리로 해서, 입력받은 좌표를 변환시켜 출력하면 끝입니다.

################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### import sys
### input == sys.stdin.readline
######################################################
N = int(input())

# data = list(map(int, input().split()))
#시간초과
#print(*[ len(set(y for y in data if x>y)) for x in data  ])
        

arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr))) # 나보다 작은 것들의 갯수 = 중복제거후 오름차순 정렬시 내 index
# value -> index를 뽑아쓸 수 있게, dict로 만든다. by dict comp
zip_dict = { arr2[i]:i for i in range(len(arr2 ))}

# 원래 배열을 돌면서, value값으로 index를 뽑아쓰면 된다.
for i in arr:
    print(zip_dict[i], end = ' ')