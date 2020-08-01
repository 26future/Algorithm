import sys
N = int(sys.stdin.readline().strip())

count = [1,2]

def count_tile(n):
    n_cnt = count[n-2]*2-1
    count.append(n_cnt)
    return

for n in range(3,N+1):
    count_tile(n)

print(count[N-1]%15746)