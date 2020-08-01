import sys
N = int(sys.stdin.readline().strip())

tile = [['0'],['00','11']]

def next_tile(n):
    n_tile = []
    for t in tile[n-2]:
        n_tile.append('1'+t)
        n_tile.append(t+'1')

    n_tile = list(set(n_tile)) # 중복 제거

    if n%2 == 0: # n이 짝수인 경우
        n_tile.append('0'*n)

    tile.append(n_tile)
    return

for n in range(3,N+1):
    next_tile(n)

print(len(tile[N-1])%15746)