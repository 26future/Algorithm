boards = [['0', '3', '5', '4', '6', '9', '2', '7', '8'], ['7', '8', '2', '1', '0', '5', '6', '0', '9'], ['0', '6', '0', '2', '7', '8', '1', '3', '5'], ['3', '2', '1', '0', '4', '6', '8', '9', '7'], ['8', '0', '4', '9', '1', '3', '5', '0', '6'], ['5', '9', '6', '8', '2', '0', '4', '1', '3'], ['9', '1', '7', '6', '5', '2', '0', '8', '0'], ['6', '0', '3', '7', '0', '1', '9', '5', '2'], ['2', '5', '8', '3', '9', '4', '7', '6', '0']]
new_boards = []
for board in boards:
    b = list(map(lambda x:int(x),board))
    new_boards.append(b)
print(new_boards)

# 각 행에서 빈 칸이 하나인 경우
def check_row(new_boards):
    # 빈 칸이 하나인 행이 더이상 없는 경우
    cnt = 0
    for row in new_boards:
        if row.count(0) == 1:
            cnt += 1
    if cnt == 0:
        return new_boards

    # 빈 칸이 하나인 행이 존재하는 경우
    for row in new_boards:
        if row.count(0) == 1:
            for number in range(1,10):
                if number not in row:
                    row[row.index(0)] = number

    check_row(new_boards)

# 열에 따른 리스트 재배치
def make_boards_column(new_boards):
    boards_column = []
    for i in range(9): # 열 인덱스
        column = []
        for board in new_boards:
            column.append(board[i])
        boards_column.append(column)
    return boards_column


# 각 열에서 빈 칸이 하나인 경우
def check_column(boards_column):
    # 빈 칸이 하나인 열이 더이상 없는 경우
    cnt = 0
    for column in boards_column:
        if column.count(0) == 1:
            cnt += 1
    if cnt == 0:
        print(boards_column)
        # 행에 따른 리스트 재배치
        new_boards = []
        for i in range(9): # 열 인덱스
            row = []
            for column in boards_column:
                row.append(column[i])
            new_boards.append(row)

        return new_boards

    # 빈 칸이 하나인 열이 존재하는 경우
    for column in boards_column:
        if column.count(0) == 1:
            for number in range(1,10):
                if number not in column:
                    column[column.index(0)] = number

    check_column(boards_column)

# 3*3 구조로 재배치
boards_square = []
list(range())
square = []
for i in range(3): # 행 인덱스
    for j in range(3): # 열 인덱스
        square.append(new_boards[i][j])
boards_square.append(square)

square = []
for i in range(3,6):
    for j in range(3,6):






# check_row(new_boards)
# print(new_boards)
# boards_column = make_boards_column(new_boards)
# print(boards_column) # 열별 리스트로 재배치
# check_column(boards_column)
# print(new_boards) # 행별 리스트로 재배치

