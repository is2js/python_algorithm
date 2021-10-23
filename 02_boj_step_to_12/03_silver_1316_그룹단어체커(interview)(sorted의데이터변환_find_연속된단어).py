# 너무 어렵게 풀었다.

# AA 핵심 -> 각 알파벳의 index를 모으고 비교가 아니라
#        -> 각 알파벳 index로 변환된 것을 기준으로 정렬하는 것을 sorted(string , key=string.find )
#        -> 연속되어있다면, key=find로 변환한 젤빠른iindex 정렬시에도 붙어있다.
# AA 연속되어있다면? 젤 빠른(앞에) index를 찾아 정렬해도 -> 같은단어 = 같은index = 줄줄이 정렬 
#       -> 연속되지 않고 떨어져있다면, 젤 빠른or젤 앞의 index기준 정렬시 뒤에것도 앞으로 땡겨져, 이상한 단어가 되어있다.

# AA sorted( key) 는 변환된 데이터(map, list comp)를 기준으로 정렬한다.
# - 여기서  string.find는 변환시, 각 문자열은 젤빠른 index로 치환되어있다.
# - 근처 붙어있다면, 그 붙은 놈들 중 젤 첫번째 index가 나오고
# - 그 index로 치환된 같은 단어들은, 정렬시 -> 같으니까 총총총 나열되어있을 것이다.
# - 만약, 떨어져있는 단어가 앞에 놈의 index로 치환되었다면? 정렬시 -> 저기 앞으로 땡겨서 총총총 정렬 -> 단어가 뭉개짐
# - 원본_string != sorted(원본, key=원본.find)

# 1. string.find() 나 sequence.index()는 제일 가까운 index만 반환한다.
# - 만약 연속되어있거나 한개라면? 똑같은 index가 총총총 나올 것이다.
# - aaabbcdd -> 000332566 / happy -> 01224
# - 만약 나왔던게 중복해서 또 나온다면? aabca -> 0024[0]
# 2. sorted(iter,  key= len/str.lower/[string원본].find/lamdba )
# - iter각 요소마다 적용될 정렬기준을 key에 함수를 인자로 넣어준다.
# - sorted(iter, key =  )로 뽑은 가장 빠른 index를 정렬기준으로 줄 수 있다.
# - happy, -> "happy".find("h") 한 것들이 기준
# - aaa의 index가 모두 같더라도, 정렬시키면 붙어서 나온다.
# 3 만약, aaabba 로 건너뛰어서 중복되어있다면?
# - sorted( key= string아무거나. find)시 
# - 뒤쪽 a도 제일빠른index기준으로 모아져 정렬된다.
# -> 처음과 다르게 정렬된다.
word = "happy" # 건너뛴 중복이 없으면 원래단어와 같다.
print(word, sorted(word, key=word.find))
# 4. sorted는 iter를 list화 시킨뒤 정렬한다. ex> 'str'->['s', 't', 'r'] 
# - dict -> [ (k1,v1), (k2,v2)]
# AAA 원본 string vs stirng list 둘중에 하나를 통합해야함.
# -> string -> list()  or list -> ''.join()
print( word ,  ''.join(sorted(word, key=word.find)))
# happy == happy

# 5. 비교시 똑같은 단어가 떨어져서 나온다면, .. 정렬시 완전 다른 단어가 되어버린다.
# -> 같은알파벳이면, 발견되는 가장빠른 index순으로 정렬시키다보니 뒤에 것을 앞으로 가져와버림.
word1 = "firefox"
print( word1 == ''.join(sorted(word1, key=word1.find)))
# firefox != ffireox





# count = 0

# n = int(input().strip())
# for _ in range(n):
#     string= input()
#     categories = set(string)
#     cate_dict = {}
#     for cate_ in categories:
#         for idx, str_ in enumerate(string):
#             if cate_ == str_:
#                 cate_dict.setdefault(cate_, []).append(idx)
    
#     check = True
#     for str_, idx_list in cate_dict.items():
        
#         if check :
#             if len(idx_list) > 1 :
#                 for i in range(1,len(idx_list)):
#                     if idx_list[i] - idx_list[i-1] != 1:
#                         check = False
                    
    
#         else:
#             break

#     if check:
#         count +=1

# print(count)
