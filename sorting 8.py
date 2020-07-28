import sys

N = int(input())
words = [sys.stdin.readline().replace('\n','') for i in range(N)]

length = [len(w) for w in words]

# key : value = index : length
idx_dict = dict()
for i in range(N):
    idx_dict[i] = length[i]

# 단어 길이(value)에 따른 오름차순 정렬
s_idx = sorted(idx_dict.items(), key=lambda x:x[1])

s_words = []
for idx in s_idx:
    s_words.append(words[idx[0]])

# 길이가 같은 단어들 내에서 정렬
sorted_words = []
for j in range(1,max(length)+1):
    same_length = []
    for word in s_words:
        if len(word) == j:
            same_length.append(word)
    same_length = sorted(list(set(same_length)))

    for w in same_length:
        print(w)