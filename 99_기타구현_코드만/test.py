# my_list = [[1, 2], [3, 4], [5, 6]]

# 1. list comp 1꺼풀 더 벗겨 콤마로 모으거나
# x = [ k for x in my_list for k in x]

# 2-1. 빈 리스트에 각 list들을 누적합해서 괄호떼고 붙히거나
# x = [] 
# for k in my_list:
#     x += k
# 2-2. 빈 리스트를 기본값으로 sum( ,[])으로 누적시키거나
# x = sum(my_list, [])

# 3-1. itertools의 chain.from_iterable 이용
# import itertools
# x = list(itertools.chain.from_iterable(my_list))
# 3-2. 1차원만 받아서 푸는 chain()에다가 사용시언패킹으로 1차원 리스트를 넘겨줌
# x = list(itertools.chain(*my_list))
# print(x)



