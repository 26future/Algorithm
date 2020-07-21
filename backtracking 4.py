numbers = input().split()
N = int(numbers[0]) # N까지의 수
M = int(numbers[1]) # 수열의 길이

numbers = list(range(1,N+1))

from itertools import combinations_with_replacement # 중복을 허용한 조합
sequences = list(combinations_with_replacement(numbers,M)) # 수열 생성

for sequence in sequences:
    print(str(sequence)[1:-1].replace(',',''))
