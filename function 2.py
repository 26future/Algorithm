self_number = list(range(1,10000))

def function_dn(n):
    number = [num for num in str(n)]
    for num in number:
        n += int(num)
    return n

n = 1
while True:
    dn = function_dn(n)
    if dn in self_number:
        self_number.remove(dn)
    if n > 10000:
        break
    n += 1

for number in self_number:
    print(number)