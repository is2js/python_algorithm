# 느낀점 : 
################ Input From input.txt ################
import sys
from pprint import pprint
sys.stdin = open("./input.txt", "rt")
######################################################


prev_ = ["***", "* *", "***"]

first_row = [x*3 for x in prev_]
# ['*********', '* ** ** *', '*********']
mid_row = [x + ' '*(9//3) + x for x in prev_]
# ['***   ***', '* *   * *', '***   ***']

# next_ = [first_row, mid_row, first_row]
# [['*********', '* ** ** *', '*********'], ['***   ***', '* *   * *', '***   ***'], ['*********', '* ** ** *', '*********']]
# '\n'.join(list)로 다 서야하기 때문에, extend로 연결만 하면된다.
next_ = first_row + mid_row + first_row
# ['*********', '* ** ** *', '*********', '***   ***', '* *   * *', '***   ***', '*********', '* ** ** *', '*********']
# print(next_)

def fractal(n):
    if n==1:
        return['*']

    prev_ = fractal(n//3)
    first_row = [x*3 for x in prev_]
    mid_row = [x + ' '*(n//3) + x for x in prev_]
    return  first_row + mid_row + first_row


print('\n'.join(fractal(81)))


    

# ********* 
# * ** ** *
# *********

# ***   ***
# * *   * *
# ***   ***

# *********
# * ** ** *
# *********

# next_

