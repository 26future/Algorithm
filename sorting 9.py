import sys

N = int(input())
members = [sys.stdin.readline().replace('\n','').split(" ") for i in range(N)]

ages = [int(a[0]) for a in members]

# key : value = index : age
m_dict = dict()
for i in range(N):
    m_dict[i] = ages[i]

# 나이 순으로 오름차순 정렬
s_age = sorted(m_dict.items(), key=lambda x:x[1])

for age in s_age:
    print(age[1],members[age[0]][1])