N = int(input())

numbers = []
for i in range(N):
    numbers.append(int(input()))

numbers = sorted(numbers)

for n in numbers:
    print(n)
