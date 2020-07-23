# N = int(input())
N = 8

board_idx = [] # 전체 체스판
for i in range(N):
    for j in range(N):
        board_idx.append([i,j])

# print(board_idx.index([4,4]))
# queen = board_idx[36] # 현재 퀸의 위치

cnt = 1
queen = board_idx[0]
inavailable = []
count = 0
def function_inavailable(cnt, board_idx):
    for idx in board_idx: # 퀸 선택
        idx = queen
        available = []

        for idx in board_idx:  # 현재 퀸의 같은 행
            if idx[0] == queen[0]:
                if idx not in inavailable:
                    inavailable.append(idx)

            if idx[1] == queen[1]: # 현재 퀸과 같은 열
                if idx == queen:
                    pass
                else:
                    if idx not in inavailable:
                        inavailable.append(idx)

        # 현재 퀸의 왼쪽 위 대각선
        row = queen[0]
        column = queen[1]
        for i in range(N):
            row -= 1
            column -= 1
            if 0 <= row < 8 and 0 <= column < 8:
                if [row,column] not in inavailable:
                    inavailable.append([row,column])

        # 현재 퀸의 오른쪽 위 대각선
        row = queen[0]
        column = queen[1]
        for i in range(N):
            row -= 1
            column += 1
            if 0 <= row < 8 and 0 <= column < 8:
                if [row,column] not in inavailable:
                    inavailable.append([row,column])

        # 현재 퀸의 왼쪽 아래 대각선
        row = queen[0]
        column = queen[1]
        for i in range(N):
            row += 1
            column -= 1
            if 0 <= row < 8 and 0 <= column < 8:
                if [row,column] not in inavailable:
                    inavailable.append([row,column])

        # 현재 퀸의 오른쪽 아래 대각선
        row = queen[0]
        column = queen[1]
        for i in range(N):
            row += 1
            column += 1
            if 0 <= row < 8 and 0 <= column < 8:
                if [row,column] not in inavailable:
                    inavailable.append([row,column])

    if cnt == N:
        return

    for idx in board_idx:
        if idx not in inavailable:
            available.append(idx)

    cnt += 1
    function_inavailable(cnt, available)
# function_inavailable() # 다음 퀸이 위치할 수 없는 인덱스 찾기


# 다음 퀸이 위치할 수 있는 인덱스 찾기
# available = []
# for idx in board_idx:
#     if idx not in inavailable:
#         available.append(idx)


# from itertools import combinations
# queens = list(combinations(board_idx,N))
# print(queens)
function_inavailable(cnt, board_idx)
print(len(inavailable))