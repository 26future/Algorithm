def solution(board, moves):
    lines = list(map(list, zip(*board)))
    basket = [0, 0]

    answer = 0
    for m in moves:
        for i in range(len(lines[m-1])):
            if lines[m-1][i] == 0:
                pass

            else:
                basket.append(lines[m-1][i])
                lines[m-1][i] = 0

                if basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    answer += 2
                    
                break

    return answer