from collections import Counter

my_str = input().strip()

cnt = Counter(my_str).most_common()
result = sorted([c[0] for c in cnt if c[1] == cnt[0][1]])

answer = ''
for r in result:
    answer += r
print(answer)