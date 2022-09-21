n = int(input())
x,y = 1,1
plans = input().split()

# L,R,U,D에 따른 이동방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획 하나씩 확인
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 : x, y가 1이나 작거나 n보다 클때
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    # 이동 수행
    x, y = nx, ny

print(x,y)