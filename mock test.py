def solution(answers):
    m1 = [1,2,3,4,5]*(len(answers)//2)
    m2 = [2,1,2,3,2,4,2,5]*(len(answers)//2)
    m3 = [3,3,1,1,2,2,4,4,5,5]*(len(answers)//2)


    count = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == m1[i]:
            count[0] += 1
        if answers[i] == m2[i]:
            count[1] += 1
        if answers[i] == m3[i]:
            count[2] += 1

    answer = list(filter(lambda x: count[x] == max(count), range(len(count))))
    answer = [a+b for a,b in list(zip(answer,[1,1,1]))]


    return answer
