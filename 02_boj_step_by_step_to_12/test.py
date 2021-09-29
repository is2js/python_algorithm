# 느낀점 : 

################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")

### input() == sys.stdin.readline()
### print() == sys.stdout.write(   + '\n')
######################################################
N = int(input())

data = [int(input()) for _ in range(N)]
data = sorted(data)
for elem in data:
    print(elem)


