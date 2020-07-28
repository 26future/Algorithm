import sys

N = int(input())
numbers = [sys.stdin.readline().split() for i in range(N)]

coordinates = list(map(lambda x:(int(x[0]),int(x[1])), numbers))
coordinates.sort(key=lambda x:(x[1],x[0]))

for c in coordinates:
    print(c[0],c[1])