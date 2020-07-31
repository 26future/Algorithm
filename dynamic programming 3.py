import sys
from itertools import permutations

N = int(sys.stdin.readline().strip())

tile = [[],['1'],['00','11']]

def next_tile(n):
    if n%2 != 0: # n이 홀수인 경우
        li = ['1']+tile[n-1]

    else: # n이 짝수인 경우
        li = ['1','11','00']+tile[n-1]

    # n번째 수열의 종류
    n_tile = list(permutations(li,2))
    n_tile = list(set(t[0]+t[1] for t in n_tile if len(t[0]+t[1]) == n))

    if n%2 == 0: # n이 짝수인 경우
        n_tile.append('0'*(n))

    tile.append(n_tile)
    return

for n in range(3,N+1):
    next_tile(n) # n번째 수열 구하기

print(len(tile[N])%15746)

