import sys

N = int(input())
numbers = [int(sys.stdin.readline().split()[0]) for i in range(N)]

count = [numbers.count(num) for num in numbers]

for num in range(1,max(numbers)+1):
    if num not in numbers:
        pass
    else:
        for j in range(count[numbers.index(num)]):
            print(num)
