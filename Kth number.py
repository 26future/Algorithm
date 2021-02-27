def solution(array, commands):

    answer = []
    for params in commands:
        i, j, k = params

        li = array[i-1:j]
        li.sort()
        answer.append(li[k-1])

    return answer
