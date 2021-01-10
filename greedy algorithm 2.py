N = int(input())
P = list(map(lambda x:int(x), input().split()))

total=0
total += sum(P)

minP = sorted(P)
for n in range(N):
    for i in range(n):
        total += minP[i]
print(total)

