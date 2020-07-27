N = 4


board_idx = [] # 전체 체스판
for i in range(N):
    for j in range(N):
        board_idx.append([i,j])


def inavailable_idx(queen):
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
        if [row,column] in board_idx:
            inavailable.append([row,column])

    # 현재 퀸의 오른쪽 위 대각선
    row = queen[0]
    column = queen[1]
    for i in range(N):
        row -= 1
        column += 1
        if [row,column] in board_idx:
            inavailable.append([row,column])

    # 현재 퀸의 왼쪽 아래 대각선
    row = queen[0]
    column = queen[1]
    for i in range(N):
        row += 1
        column -= 1
        if [row,column] in board_idx:
            inavailable.append([row,column])

    # 현재 퀸의 오른쪽 아래 대각선
    row = queen[0]
    column = queen[1]
    for i in range(N):
        row += 1
        column += 1
        if [row,column] in board_idx:
            inavailable.append([row,column])

    global available
    available = [] # 다음 행에서 퀸으로 가능한 위치
    for j in range(N):
        if [queen[0]+1,j] not in inavailable:
            available.append([queen[0]+1,j])

    return
# print(inavailable)
# print(available)
# print("="*30)


# 1행부터 마지막 행까지
def next_queen(row):
    for queen in available:
        # print('row:',row)
        # print(queen)
        inavailable_idx(queen)
        # print('inavailable:',inavailable)
        # print("available:",available)
        # print('-'*30)

        if len(available) == 0: # 다음 행을 고려하지 않는 경우
            pass
        elif row == N-1:
            global count
            count += 1
            # print('count:', count)
            return
        else:
            row += 1
            next_queen(row)

    return



queens = [[0,i] for i in range(N)]
total_count = 0

for queen in queens:
    inavailable = []
    inavailable_idx(queen)  # 0행에 대한 시행

    row = 1
    count = 0

    next_queen(row) # 1행부터 마지막 행까지
    total_count += count

print(total_count)








