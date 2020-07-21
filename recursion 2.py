N = int(input())

sequence = [0,1]
n = 2
def fibonacci(n):
    tmp = sequence[n-1]+sequence[n-2]
    sequence.append(tmp)
    if n == N:
        return
    n += 1
    fibonacci(n)

fibonacci(n)
print(sequence[N])

