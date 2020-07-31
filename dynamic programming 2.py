import sys
T = int(input())

def fibonacci(n):
    if n == 0:
        global count_0
        count_0 += 1
        return 0

    elif n == 1:
        global count_1
        count_1 += 1
        return 1

    else:
        return fibonacci(n-1)+fibonacci(n-2)


numbers = [int(sys.stdin.readline().replace('\n','')) for i in range(T)]
for N in numbers:
    count_0 = 0
    count_1 = 0

    fibonacci(N)
    print(count_0,count_1)

