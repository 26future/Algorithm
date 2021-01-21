import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
numbers = [list(map(str, list(range(1,10))))]


def stair_numbers(cnt):
    if cnt == 0:
        return

    new = []
    for n in numbers[-1]:
        if n[-1] == '9':
            new.append(n+'8')
        elif n[-1] == '0':
            new.append(n+'1')
        else:
            new.append(n + str(int(n[-1])-1))
            new.append(n + str(int(n[-1])+1))

    cnt -= 1
    numbers.append(new)
    del new
    stair_numbers(cnt)


cnt = N-1

stair_numbers(cnt)
print(divmod(len(numbers[-1]),1000000)[1])

