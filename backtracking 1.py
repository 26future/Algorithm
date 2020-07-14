numbers = input().split()
N = int(numbers[0]) # N까지의 수
M = int(numbers[1]) # 수열의 길이

numbers = [n for n in range(1,N+1)]

from itertools import permutations
sequences = list(permutations(numbers,M))

for sequence in sequences:
    print(str(sequence)[1:-1].replace(',',''))