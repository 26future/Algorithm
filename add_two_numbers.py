from itertools import combinations


def solution(numbers):
    two_numbers = list(combinations(numbers, 2))

    answer = []
    for num in two_numbers:
        answer.append(num[0] + num[1])

    answer = sorted(list(set(answer)))

    return answer