while True:
    try:
        a,b = input().split()
        print(int(a)+int(b))
    except: # 입력값이 없는 경우
        break

