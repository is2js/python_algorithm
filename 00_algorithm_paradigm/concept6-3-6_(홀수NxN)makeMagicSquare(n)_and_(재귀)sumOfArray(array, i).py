#### checkMagic : NxN 마방진의 행합 -> 열합 -> 대각선2개합 같은지 확인하기
def checkMagic(square):
    # 1. 기준을 0번째 행합으로 잡아두기
    magic = 0
    for j in range(len(square)):
        # 열을 돌거니까 행은 0으로 고정해놓고, 열만 돌기
        magic += square[0][j]

    # 2. 정방행렬 가정하에, i -> j순으로 돌리되, 행고정 열탐색 & 열고정 행탐색을 동시에 한다.
    # -> 바깥for: 각~마다 , 안쪽for: ~를 탐색해서  &  누적합을 구함.
    for i in range(len(square)):
        # squarep[i][?] -> 각 행마다
        # squarep[?][i] -> 각 열마다 
        # *2차원 배열의 접근은 행부터 해야하지만, 이중for문이라면 고정은 열부터 할 수 있다.
        # by 바깥for문을 [][i] 열자리에 고정시켜서 -> 행 탐색을 시킬 수 있다.
        row_sum = 0
        col_sum = 0
        for j in range(len(square)):
            row_sum += square[i][j] # 각 행마다,열 탐색중
            col_sum += square[j][i] # 바깥 i가 열자리에 -> 각 열마다, 행 탐색중

        # 3. 여기선, 각 행합row_sum, 각 열합 col_sum이 완성된 상태다.
        # - 각 행합, 각 열합들이 구해질 때마다, 기준magic과 다른지 확인함.
        if row_sum != magic or col_sum != magic:
            return False

    # 4. 각 행합 = 각 열합 = magic(기준)이 통과되었다면, 대각선도 검사한다.
    # -> 대각선의 움직임은 항상  <위or아래부터 결정> -> 좌우는  좌->우 로만 움직인다 생각하고
    # * 1) row가 올라가는지 vs 내려가는지(index에 -를 단 등차수열_index 새로 만들기)
    # 2) col은 왼쪽에서 오른쪽으로 가니까 항상 그대로다.
    # 3) 2개의 대각선은 row, col_index가  같은 경우가 많아, 1개의 for문으로  탐색 된다.
    
    # 4-4) 대각선의 합도, 탐색하며 누적합으로 구한다.
    d_sum = 0
    d2_sum = 0
    for d in range(len(square)):
        d_sum += square[d][d] # 4-1) 내려가는 대각선 아래로(row) & 오른쪽으로

        d2 = -d + (len(square)-1) # 4-2) 올라가는(row)는 새로운 -1이 등차, 첫항은 d=0시 n-1 index에서 시작 하도록, 등차수열로 새로운 index를 만든다.
        # 4-3) 대각선의 좌우움직임은 항상 좌->우(1씩 증가) 이므로 d 그대로 간다.
        d2_sum += square[d2][d]
    
    # 5. 대각선 합 검사
    if d_sum != magic or d2_sum!=magic:
        return False

    # 6. 다 통과는 return True 
    return True

    
    


        
#### 홀수 NxN 마방진 채우기
# 0. 2차원 행렬을 미리 만들어놓고 채운다.
# 1. 0행 가운데 원소에 1을 넣고 시작한다.
# 2. 1부터 n**2까지 for를 돌면서 채워나간다.
# 3. 상(row-=1/좌col-=1)로 이동해서 다음 수를 채우는데, 이미 차있으면 다시 돌아와(row+=1/col+=1), 한칸 아래(row+=1)에 채워준다.
# * 상or좌로 배열을 <-음수로 빼다 넘어가면> -> n(배열길이)만 더하면, 반대 자리로 이동한다.
# * 하or우로 배열을 <양수로 더하다 넘어가면> -> %n(배열길이로 나눈 나머지)로 대체 하면, 반대 자리로 이동한다.
# * 매번 이동시마다 검사를 해줘야한다.
def makeMagicSquare(n):
    # 1. 미리 배열을 만든다. 이미 정해져있다.
    square = [[0]*n for _ in range(n)]

    # 2. row, col index의 시작점을 찍어주고 투포인터로 행렬을 돌아다닌다.
    row = 0
    col = n//2 # 홀수니까 정확히 가운데다
    
    # 3. 1부터 채워나갈 준비를 한다. 이미 첫번째 인덱스가 있으니 포인터 옮기기전에 채우고 시작한다.
    for k in range(1, n**2 +1):
        square[row][col] = k 

        # 3-1. 위/좌로 이동했다면, 음수넘어감 검사부터 한다.
        row-=1 
        if row<0: row += n
        col-=1
        if col<0: col += n

        # # 이미 그 인덱스가 이미 차있다면? 돌아감+ 한칸 아래로 이동한다.
        # # -> 더하고 나서  오른쪽으로 넘어갈 때 검사도 해준다.
        if square[row][col] != 0:
        #     row+=2
        #     col+=1
        #     # 마지막 인덱스를 넘어갔따면, 구간으로 나눈 나머지로 이동시켜준다.
        #     if row > n-1:row = row % n 
        #     if col > n-1:col = col % n 
        
            # * 배열에서 <n-1 index보다 우측으로 넘어가지 않는다면>
            # -> % n(구간)으로 나눈 나머지를 할당해도 똑같은 자리에 멈춰있으므로
            # * -> 넘어갈 가능성이 있다면, 그냥 구간으로 나눈 나머지를 배정해줘버리자.
            row = (row+2) % n  # * 배열index의 +1, +2는 넘어갈 가능성이 있으므로, if로 가르지말고 그냥 구간으로 나눈 나머지를 줘버리면 알아서 처리된다.
            col = (col+1) % n  

    return square

print("1. makeMagicSquare(5) :>>")
for row in makeMagicSquare(5):
    print(*row)

print()
print()

print("2. checkMagic(makeMagicSquare(5)) :>>", checkMagic(makeMagicSquare(5)))
    



