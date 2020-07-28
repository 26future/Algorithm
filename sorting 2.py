import sys

N = int(input())
numbers = [sys.stdin.readline().replace('\n','') for i in range(N)]
numbers = list(map(lambda x:int(x), numbers))
numbers = sorted(numbers)

for number in numbers:
    print(number)