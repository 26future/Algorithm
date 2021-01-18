import sys

N = int(sys.stdin.readline())

meetings = []
for i in range(N):
    time = tuple(map(int, sys.stdin.readline().split()))
    meetings.append(time)

meetings.sort(key=lambda x:(x[1],x[0]))
first = meetings[0]

cnt = 1
for j in range(1,N):
    if first[1] <= meetings[j][0]:
        first = meetings[j]
        cnt += 1
print(cnt)


