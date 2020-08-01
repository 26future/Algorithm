import sys
N = int(sys.stdin.readline().strip())

count = [0]*1000001
count[0] = 1
count[1] = 2

for n in range(3,N+1):
    count[n-1] = 2*count[n-2]-1

print(count[n-1]%15746)