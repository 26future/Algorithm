import sys
from collections import Counter

N = int(input())
numbers = [int(sys.stdin.readline().split()[0]) for i in range(N)]

cnt_numbers = dict(Counter(numbers))

# 개수 세기
s_numbers = sorted(cnt_numbers.items())

for num in s_numbers:
    for j in range(num[1]):
        print(num[0])