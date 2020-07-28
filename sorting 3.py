import sys

N = int(input())
numbers = [int(sys.stdin.readline().split()[0]) for i in range(N)]


for num in list(set(numbers)):
    for j in range(numbers.count(num)):
        print(num)
