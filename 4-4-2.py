# 캐릭터가 방문한 칸 구하기

# n,m을 공백으로 구분하여 입력받기
n,m = map(int, input().split())

# 현위치좌표와 방향 입력받기
x, y, direction = map(int, input().split())

# 맵 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 이미 가본 곳 표시하는 맵
d = [[0] * m for _ in range(n)]
# 현위치 가본 곳으로 표시하기
d[x][y] = 1

# 북동남서 방향
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 도는 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
rotate = 0
count = 1
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dx[direction]
    # 왼쪽으로 회전해 한발자국 있는 곳이 가보지않은 곳인 동시에 육지이면
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        # 현위치 update
        x = nx
        y = ny
        # 가본곳으로 표시
        d[nx][ny] = 1
        rotate = 0
        # 한발짝 움직임
        count += 1
    # 가본 곳이거나 바다이면
    else:
        # 그냥 회전만 하기 (4번 돌때까지)
        rotate += 1
    # 4번을 돌아도 이미 가본 칸이거나 바다로 되어있다면
    if rotate == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 물러나도 육지라면 현위치 update (물러나기)
        if d[nx][ny] == 0 :
            x = nx
            y = ny
        # 뒤가 바다라면 break
        else:
            break
        # 다시 맨처음 rotate 로 초기화
        rotate = 0

print(count)