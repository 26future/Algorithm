import sys
from itertools import permutations

N = int(sys.stdin.readline().strip())

tile = [['1'],['00','11']]

def next_tile(i):
    li = tile[i].copy()
    li.append('1')

    if i%2 == 0: # n이 짝수인 경우
        li.append('00')
        li.append('11')

    # n번째 수열의 종류
    new_tile = list(permutations(li,2))
    new_tile = [t[0]+t[1] for t in new_tile]

    new_tile = [t for t in new_tile if len(t) == i+2]

    if i%2 == 0: # n이 짝수인 경우
        new_tile.append('0'*(i+2))

    tile.append(list(set(new_tile)))

    return

for n in range(2,N): # n은 인덱스
    next_tile(n-1)

print(len(tile[N-1])%15746)