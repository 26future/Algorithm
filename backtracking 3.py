numbers = input().split()
N = int(numbers[0]) # N까지의 수
M = int(numbers[1]) # 수열의 길이

num_list = []
numbers = [n for n in range(1,N+1)]

for i in range(M):
    num_list.append(numbers)

from itertools import product
sequences = list(product(*num_list))

for sequence in sequences:
    print(str(sequence)[1:-1].replace(',',''))