# 느낀점 : 
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################
# https://nanarin.tistory.com/203 -> 3번째 풀이 참고
# 느낀점
# - 문자열은 재귀시 바로 append 등 n//3 으로 n모양을 만들도록 append extend 등을 할 수가 없다.
# - 각 줄바꿈 단위별로 잘라서 1차원을 만든다. -> 나중에 join시 \n로 join하면 line다 다 선다.
# **- 부분문제를 변수로 받아서 처리하기도 한다.**
# ** 문자열의 재귀는 '\n'.join으로 다 세울거니까 --> 1차원 list로 요소들을 다 만들면된다.**

N= int(input()) # 그 당시(제일 큰)의 빈 행렬을 만들기 위해 받아놓고 바로 처리

