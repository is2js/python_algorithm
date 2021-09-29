# find 함수와 index 함수의 비교
# find 함수는 문자열에서만 사용 가능한 함수이다. 이와 유사한 기능을 하는 함수로 index 함수가 있다. index 함수는 문자열뿐만 아니라 리스트, 튜플과 같은 반복 가능한 iterable 자료형에서도 찾는 문자의 인덱스를 반환하는 함수로 쓰인다. find 함수와 다른 점은 find 함수는 찾는 문자가 문자열 안에 포함되지 않은 경우 -1을 출력하지만 index함수는 >AttributeError가 발생한다.

# 내풀이
# - string.index(), list.index() 모두 작동하지만 
# - find()와 달리, .index()는 값이 없을 때는 ValueError에러를 발생한다.
# - 그래서 try, except를 씀.

# import string
# S = list("baekjoon")
# for k in string.ascii_lowercase:
#     try :
#         n = S.index(k)
#         print(n, end=' ')
#     # ValueError: 'c' is not in list
#     except:

#         print(-1, end=' ')


# sequence.index()말고, string.find()를 쓰면?
# - string.find()에 값이 없을 경우 -1을 반환한다.
import string
S = "baekjoon"
for k in string.ascii_lowercase:
    n = S.find(k)
    print(n, end=' ')



         
