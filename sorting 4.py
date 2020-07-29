import sys
from collections import Counter

N = int(input())
numbers = [sys.stdin.readline().replace('\n','') for i in range(N)]
numbers = list(map(lambda x:int(x), numbers))

# 산술평균
mean = sum(numbers)/N
print(round(mean))

# 중앙값
s_numbers = sorted(numbers)
median = s_numbers[N//2]
print(median)

# 최빈값
cnt_numbers = Counter(s_numbers).most_common()
max_count = max([cnt[1] for cnt in cnt_numbers])

if len(cnt_numbers) > 1:
    if cnt_numbers[1][1] == max_count:
        print(cnt_numbers[1][0])
    else:
        print(cnt_numbers[0][0])

else: # 입력된 수가 1개인 경우
    print(cnt_numbers[0][0])

# 범위
print(max(s_numbers)-min(s_numbers))