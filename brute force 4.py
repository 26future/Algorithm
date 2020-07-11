numbers = input().split()
N = int(numbers[0]) # 세로
M = int(numbers[1]) # 가로

square = []
for i in range(N): # 전체 보드 패턴
    colors = input()
    square.append(colors)

chess_boards = [] # 잘라낸 체스판
for n in range(N-7): # 행 슬라이싱
    square_row = square[n:n+8]

    for m in range(M-7): # 열 슬라이싱
        board=[]

        for row in square_row:
            square_column = row[m:m+8]
            board.append(square_column)
        chess_boards.append(board)

counts = [] # 다시 칠해야 하는 개수
for board in chess_boards:

    # 첫번째 칸이 W인 경우
    count1 = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 != 0 and board[i][j] != 'B': # 합이 홀수 : B
                count1 += 1
            elif (i+j) % 2 ==0 and board[i][j] != 'W': # 합이 짝수 : W
                count1 += 1
            else:
                pass
    counts.append(count1)

    # 첫번째 칸이 B인 경우
    count2 = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0 and board[i][j] != 'B': # 합이 짝수 : B
                count2 += 1
            elif (i+j) % 2 !=0 and board[i][j] != 'W': # 합이 홀수: W
                count2 += 1
            else:
                pass
    counts.append(count2)

print(min(counts))

