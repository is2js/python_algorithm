paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"

# 문장에서 대+소문자+숫자만 남기기 -> \w 를 제외한 것들 다 제거 -> [^]를 활용한 반대 모두 제거시 공백까지 제거하면 붙어버림 -> 형태유지를 위해 공백으로 제거
import re 
# words = re.sub("[^\w]", " ", paragraph).split()
# 문장은 쪼개기전에 미리 소문자로 바꿔두자. for 단어카운팅
words = re.sub("[^\w]", " ", paragraph).lower().split()


# list에서 삭제할 원소가 있다면?  set으로 만들어놓고 not in 필터링으로 제거하기
remove_set = {'hit'}
words =[word for word in  words  if word not in remove_set]

from collections import Counter

counts = Counter(words)
max_word  = counts.most_common()[0][0] # 최대cnt 중복 확인필요
max_word