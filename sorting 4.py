import sys

N = int(input())
numbers = [sys.stdin.readline().replace('\n','') for i in range(N)]
numbers = list(map(lambda x:int(x), numbers))

# 산술평균
mean = sum(numbers)/N
print(round(mean))

# 중앙값
s_numbers = sorted(numbers)
median = s_numbers[N//2]
print(median)

# 최빈값
count = [s_numbers.count(n) for n in s_numbers]
max_numbers = []
for n in s_numbers:
    if s_numbers.count(n) == max(count):
        max_numbers.append(n)

s_numbers = sorted(max_numbers)
if len(s_numbers) != 1:
    print(s_numbers[1])
else:
    print(s_numbers[0])

# 범위
print(max(s_numbers)-min(s_numbers))