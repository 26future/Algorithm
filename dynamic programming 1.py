N = int(input())

sequence = [0,1]

# n번째 피보나치 수를 구하는 함수
def new(i):
    sequence.append(sequence[i-2]+sequence[i-3])
    return

for n in range(3,N+2):
    new(n)

print(sequence[N])