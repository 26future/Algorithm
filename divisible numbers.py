def solution(arr, divisor):
    answer = [n for n in arr if n % divisor == 0]
    answer.sort()

    if len(answer) == 0:
        answer = [-1]

    return answer