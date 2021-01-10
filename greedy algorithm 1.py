N,K = input().split()
K = int(K)

coins=[]
for i in range(int(N)):
    coins.append(int(input()))

coins.reverse()
n=0
for c in coins:
    m = K // c
    K = K - c*m
    n+=m
print(n)
