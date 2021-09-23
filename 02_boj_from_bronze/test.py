################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################
N = input()


for x in range(1, int(N)):
    if (x + sum([ int(k) for k in str(x)])) == int(N):
        print(x) 
        break

else:
    print(0)