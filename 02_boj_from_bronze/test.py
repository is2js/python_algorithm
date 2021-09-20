# 느낀점 : 
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################
N = int(input())


def func(n):
    k = n//3
    matrix = [ [func(k)] * k for _ in range(k)] 
    matrix[k:k+1][k//2] = ' '
    return '\n'.join([ ''.join(row) for row in matrix])
# 재귀적으로 되려면,, 첫번째 것도. append식으로 채워할듯하다.
# - 문자열로는답이 없다. -> 행렬로 처리
n=9
k = n//3
matrix = [ [func(3)] * k for _ in range(k)] 

func(9)