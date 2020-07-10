numbers = input().split()
N = int(numbers[0]) # 세로
M = int(numbers[1]) # 가로

square = []
for i in range(N): # 전체 보드 패턴
    colors = input()
    square.append(colors)

chess_boards = [] # 잘라낸 체스판
for n in range(N-7):b
    for m in range(M-7):
        chess_board = square[n:n+8][m:m+8]
        chess_boards.append(chess_board)

# chess_boards = [['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBBBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']]



counts = [] # 다시 칠해야 하는 개수
for board in chess_boards:
    print(board)

#     # 첫번째 칸이 W인 경우
#     count1 = 0
#     for i in range(8):
#         for j in range(8):
#             if (i+j) % 2 != 0 and board[i][j] != 'B': # 합이 홀수 : B
#                 count1 += 1
#             elif (i+j) % 2 ==0 and board[i][j] != 'W': # 합이 짝수 : W
#                 count1 += 1
#             else:
#                 pass
#     counts.append(count1)
#
#
#
#
#     # 첫번째 칸이 B인 경우
#     count2 = 0
#     for i in range(8):
#         for j in range(8):
#             if (i+j) % 2 == 0 and board[i][j] != 'B': # 합이 짝수 : B
#                 count2 += 1
#             elif (i+j) % 2 !=0 and board[i][j] != 'W': # 합이 홀수: W
#                 count2 += 1
#             else:
#                 pass
#     counts.append(count2)
#
#
#
# print(min(counts))
#
