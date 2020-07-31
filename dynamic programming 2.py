import sys
T = int(sys.stdin.readline().strip())

def fibonacci(i):
    i_count = [count[i-2][0]+count[i-1][0], count[i-2][1]+count[i-1][1]]
    count.append(i_count)
    return

for i in range(T):
    n = int(sys.stdin.readline())

    # [0의 개수, 1의 개수]
    count = [[1, 0], [0, 1]]

    for j in range(2,n+1):
        fibonacci(j)

    print(count[n][0],count[n][1])
