N = int(input())
li = []
for i in range(N):
    n = int(input())
    li.append(n)

for idx in range(1, N):
    for j in range(li.index(li[idx])):
        if li[j] <= li[idx]:
            pass
        else:
            a = li[j]
            b = li[idx]
            li[idx] = a
            li[j] = b

for number in li:
    print(number)