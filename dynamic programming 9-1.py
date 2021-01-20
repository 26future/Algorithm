import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

numbers = list(map(str, list(range(1,10))))

def stair_numbers(numbers):
    new = []
    for n in numbers:
        if n[-1] == '9':
            new.append(n+'8')
        elif n[-1] == '0':
            new.append(n+'1')
        else:
            new.append(n + str(int(n[-1])-1))
            new.append(n + str(int(n[-1])+1))

    del numbers
    numbers = new[:]
    del new
    return numbers


for i in range(N-1):
    numbers = stair_numbers(numbers)

print(divmod(len(numbers),1000000000)[1])
