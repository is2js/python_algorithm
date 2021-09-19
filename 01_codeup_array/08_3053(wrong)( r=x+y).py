################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################
r = int(input())

from math import pi
print(round(pi * (r**2), 6))

print(f"{((2*r)**2)/2:.6f}")
