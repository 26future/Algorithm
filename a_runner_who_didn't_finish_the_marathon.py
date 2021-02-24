from collections import Counter

def solution(participant, completion):

    diff = Counter(participant) - Counter(completion)
    answer = list(diff.elements())[0]

    return answer