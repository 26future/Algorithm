N = int(input()) # 수의 개수
numbers = input().split() # 수열
numbers = list(map(lambda x:int(x), numbers))
operators_cnt = input().split() # 연산자 개수
operators_cnt = list(map(lambda x:int(x), operators_cnt))

operators = ['+','-','*','//']

operator_list = []
for i in range(4):
    for j in range(operators_cnt[i]):
        operator_list.append(operators[i])

from itertools import permutations
operator_sequence = set(list(permutations(operator_list, len(operator_list))))

results = []
for operators in operator_sequence:
    cal = numbers[0]
    for i in range(N-1):
        if operators[i] == '+':
            cal += numbers[i+1]
        elif operators[i] == '-':
            cal -= numbers[i+1]
        elif operators[i] == '*':
            cal *= numbers[i+1]
        elif operators[i] == '//':
            if cal < 0 and numbers[i+1] > 0:
                cal = -((-cal) // numbers[i+1])
            else:
                cal = cal // numbers[i+1]
    results.append(cal)

print(max(results))
print(min(results))
