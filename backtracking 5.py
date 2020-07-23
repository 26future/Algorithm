# N = int(input())
N = 8

board_idx = [] # 전체 체스판
for i in range(N):
    for j in range(N):
        board_idx.append([i,j])

# print(board_idx.index([4,4]))
# queen = board_idx[36] # 현재 퀸의 위치


def next_queen(cnt):
    for idx in board_idx:  # 현재 퀸의 같은 행
        if idx[0] == queen[0]:
            inavailable.append(idx)

        if idx[1] == queen[1]: # 현재 퀸과 같은 열
            if idx == queen:
                pass
            else:
                inavailable.append(idx)

    # 현재 퀸의 왼쪽 위 대각선
    row = queen[0]
    column = queen[1]
    for i in range(N):
        row -= 1
        column -= 1
        if 0 < row < 9 and 0 < column < 9:
            inavailable.append([row,column])

    # 현재 퀸의 오른쪽 위 대각선
    row = queen[0]
    column = queen[1]
    for i in range(N):
        row -= 1
        column += 1
        if 0 < row < 9 and 0 < column < 9:
            inavailable.append([row,column])

    # 현재 퀸의 왼쪽 아래 대각선
    row = queen[0]
    column = queen[1]
    for i in range(N):
        row += 1
        column -= 1
        if 0 < row < 9 and 0 < column < 9:
            inavailable.append([row,column])

    # 현재 퀸의 오른쪽 아래 대각선
    row = queen[0]
    column = queen[1]
    for i in range(N):
        row += 1
        column += 1
        if 0 < row < 9 and 0 < column < 9:
            inavailable.append([row,column])

    if cnt == N:
        return

    cnt += 1
    next_queen(cnt)


from itertools import combinations
global cnt
result = []

for idx in board_idx:
    inavailable = [] # 다음 퀸이 위치할 수 없는 인덱스
    cnt = 1
    queen = idx
    next_queen(cnt)
    # print(len(inavailable))

    available = []
    for idx in board_idx:
        if idx not in inavailable:
            available.append(idx)

    queens = list(combinations(available,N))

print(len(queens))




# print(len(inavailable))
# # print(set_inavailable)
#
# available = []
# for idx in board_idx:
#     if idx not in inavailable:
#         available.append(idx)
#
# print(available)
# print(len(available))

# from itertools import combinations
# queens = list(combinations(available,N))
# print(len(queens))

# for idx in board_idx: # 현재 퀸의 같은 행
#     if idx[0] == queen[0]:
#         inavailable.append(idx)
#
# # print(inavailable)
#
# for idx in board_idx: # 현재 퀸과 같은 열
#     if idx[1] == queen[1]:
#         inavailable.append(idx)
#
# row = queen[0]
# column = queen[1]
#
# # 현재 퀸의 왼쪽 위 대각선
# for i in range(N):
#     row -= 1
#     column -= 1
#     if 0 < row < 9 and 0 < column < 9:
#         inavailable.append([row,column])
#
# # 현재 퀸의 오른쪽 위 대각선
# for i in range(N):
#     row -= 1
#     column += 1
#     if 0 < row < 9 and 0 < column < 9:
#         inavailable.append([row,column])
#
# # 현재 퀸의 왼쪽 아래 대각선
# for i in range(N):
#     row += 1
#     column -= 1
#     if 0 < row < 9 and 0 < column < 9:
#         inavailable.append([row,column])
#
#
# # 현재 퀸의 오른쪽 아래 대각선
# for i in range(N):
#     row += 1
#     column += 1
#     if 0 < row < 9 and 0 < column < 9:
#         inavailable.append([row,column])
#
# print(inavailable)