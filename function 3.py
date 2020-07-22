N = int(input())

def sequence(number, cnt):
    number = str(number)
    difference = []
    for i in range(len(number)-1): # 각 자리수의 차
        difference.append(int(number[i])-int(number[i+1]))

    if difference[0] == difference[-1]: # 등차수열을 이루는 경우
        cnt += 1

    return cnt

cnt = 0
for n in range(1,N+1):
    if n < 100: # 한자리, 두자리 자연수는 모두 한수(등차수열)
        cnt += 1
    else:
        cnt = sequence(n,cnt)

print(cnt)