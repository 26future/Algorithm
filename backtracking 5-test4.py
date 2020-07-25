N = 4

# board_idx = [] # 전체 체스판
# for i in range(N):
#     for j in range(N):
#         board_idx.append([i,j])

# global count
queen = [0,1]
# count = 0
inavailable_column = []
inavailable_column.append(queen[1])

def next_row(queen):
    global available
    available = []
    for j in range(N):
        if j in inavailable_column: # 퀸과 같은 열에 위치
            pass
        elif j == queen[1]-1: # 왼쪽 아래 대각선
            pass
        elif j == queen[1]+1: # 오른쪽 아래 위치
            pass
        else:
            available.append([queen[0]+1,j])

    if len(available) == 0: # 다음 행을 고려하지 않는 경우
        inavailable_column.remove(queen[1])

    return

next_row(queen) # 0행에 대한 시행

count = 0
# 1행부터 마지막 행까지
row = 1
def next_queen(row,count):
    for queen in available:
        print(queen)
        inavailable_column.append(queen[1])
        next_row(queen)
        print('row:',row)
        print(available)
        if len(available) == 0: # 다음 행을 고려하지 않는 경우
            pass
        else:
            print('-'*30)
            row += 1
                # print(count)
            next_queen(row,count)
            if row == N - 1:
                count += 1
                print(count)


    return

next_queen(row,count)
# print(count)
