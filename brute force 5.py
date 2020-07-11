N = int(input())

num = 0  # 1부터 숫자 카운트
count = 0  # 종말의 숫자 순서
while True:
    if '666' in str(num):
        count += 1
    if count == N:
        break
    num += 1

print(num)
