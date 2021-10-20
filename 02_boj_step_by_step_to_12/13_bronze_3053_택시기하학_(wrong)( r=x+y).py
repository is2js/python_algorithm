# 느낀점 
# - 문제를 잘 해석해야하는데, 그게 잘안됬다.
# - 택시기하학에서의 두점사이거리 -> 거기에 한쌍은 특정좌표x1,y1그대로두고, 한쌍만 x,y로 두면 원의 방정식 -> 
# -> 거기에 x1, y1을 0,0으로 두면 쉽게 넓이가 계산된다.
# - r= |x| + |y|의 그림은? x>0, y>0 1사분면만 먼저 생각해서 다이아몬드로 그리면 된다.
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################
r = int(input())

from math import pi
print(round(pi * (r**2), 6))

print(f"{((2*r)**2)/2:.6f}")
