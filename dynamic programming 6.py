import sys

n = int(sys.stdin.readline().strip())
triangle = [sys.stdin.readline().split() for i in range(n)]


# int형으로 변경
for i in range(n):
    triangle[i] = list(map(lambda x:int(x), triangle[i]))

# 부분합
p_sum = [0]*n
p_sum[0] = triangle[0][0]
p_sum[1] = [p_sum[0]+triangle[1][0],p_sum[0]+triangle[1][1]]

# 해당 row 까지의 합 구하기
for row in range(2,len(triangle)):
    tmp_sum = [0]*(row+1)

    for j in range(len(triangle[row])): # 각 줄에서 숫자의 인덱스
        num = triangle[row][j] # 현재 숫자

        if j == 0: # 각 줄의 첫번째 숫자 (한가지 경우의 수 존재)
            tmp_sum[0] = num+p_sum[row-1][0]

        elif j == len(triangle[row])-1: # 각 줄의 마지막 숫자 (한가지 경우의 수 존재)
            tmp_sum[-1] = num+p_sum[row-1][-1]

        else: # 두 가지의 경우의 수 존재, 최대값 선택
            tmp_sum[j] = max([num+p_sum[row-1][j],num+p_sum[row-1][j-1]])

    p_sum[row] = tmp_sum

print(max(p_sum[-1]))
