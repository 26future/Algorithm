import math

numbers = [int(input()) for i in range(5)]

pow_num = 1
for num in numbers:
    pow_num *= num

    if math.sqrt(pow_num).is_integer():
        print('found')
        break

else:
    print('not found')
