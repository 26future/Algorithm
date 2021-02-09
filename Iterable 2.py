def solution(mylist):
    answer = []
    for n1, n2 in list(zip(mylist, mylist[1:])):
        a = abs(n1 - n2)
        answer.append(a)
    return answer