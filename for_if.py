def solution1(mylist):
    answer = []
    for num in mylist:
        if num % 2 == 0:
            answer.append(pow(num, 2))

    return answer



def solution2(mylist):
    answer = [pow(num,2) for num in mylist if num%2 == 0]

    return answer
