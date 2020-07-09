import sys

T = int(input())

for i in range(T):
    number = list(map(int, sys.stdin.readline().split()))
    print(number[0]+number[1])