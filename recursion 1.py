N = int(input())

res = 1
def factorial(n):
    global res
    res *= n

    if n == 1:
        return res

    n -= 1
    factorial(n)

factorial(N)
print(res)

# for n in range(1,N+1):
#     res *= n
# print(res)
