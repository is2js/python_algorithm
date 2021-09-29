import sys
sys.setrecursionlimit(100000)

input=sys.stdin.readline

N = int(input().strip())

if N==1:
    paper = [[int(input().strip())]]
else:
    paper = [ list(map(int, input().strip().split())) for i in range(N)]

count_dict = {}

def check_valid(matrix):
    global count_dict
    if len(matrix) == 1:
        # 1개짜리라면..  넣고 +1
        count_dict.setdefault(matrix[0][0], 0)
        count_dict[matrix[0][0]] +=1
        return True

    
    paper_0_0 = matrix[0][0]
    flag = False
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if paper_0_0 != matrix[i][j]:
                flag = True
                break
    if flag:
        N = len(matrix)
        
        # 3x3중 1x1 -> 열 3구간 다 
        check_valid([ row[:N//3] for row in matrix[:N//3]])
        check_valid([ row[N//3:(N//3)*2] for row in matrix[:N//3]])
        check_valid([ row[(N//3)*2:] for row in matrix[:N//3]])
        # 3x3중 2x2
        check_valid([ row[:N//3] for row in matrix[N//3:(N//3)*2]])
        check_valid([ row[N//3:(N//3)*2] for row in matrix[N//3:(N//3)*2]])
        check_valid([ row[(N//3)*2:] for row in matrix[N//3:(N//3)*2]])
        # 3x3중 3x3
        check_valid([ row[:N//3] for row in matrix[(N//3)*2:]])
        check_valid([ row[N//3:(N//3)*2] for row in matrix[(N//3)*2:]])
        check_valid([ row[(N//3)*2:] for row in matrix[(N//3)*2:]])
    else:
        count_dict.setdefault(paper_0_0, 0)
        count_dict[paper_0_0] += 1
        return True



check_valid(paper)

for key in [-1,0,1]:
    count_dict.setdefault(key, 0)
print(*map(lambda x:x[1], sorted(count_dict.items(), key=lambda x:x[0])))