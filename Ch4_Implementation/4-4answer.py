# n,m을 공백으로 구분하여 입력받기 (N*M 형태의 맵)
n,m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x, y좌표, 방향 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

array = []
for i in range(n):
    array.append(list(map(int, input(i).split())))

# 순서대로 북,동,남,서 방향 정의 (맵에서의 x,y는 다르다)

# 북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 회전 (direction을 바꾸기 : 북동남서 0123)
def turn_left():
    global direction
    direction -= 1
    if direction == -1 :
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 이후 정면에 가보지 않은 칸이면서 육지인경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        # 방문 표시
        d[nx][ny] = 1
        # 업데이트
        x = nx
        y = ny
        count += 1
        turn_time = 0

    # 가본 칸이거나 바다인경우
    else:
        # 회전만 했다는 표시 + 위로 올라가서 회전하고 if 문 전에 걸리니까
        turn_time += 1
    # 4번회전만 했다면 > 네 방향 모두 가본칸이거나 바다인경우
    if turn_time == 4:
        # 방향그대로 뒤로 물러서기 (갈 방향 미리 지정)
        nx = x-dx[direction]
        ny = y-dy[direction]
        # 뒤가 육지라면 x,y 업데이트 (뒤로 이동하기)
        if array[nx][ny] == 0 :
            x = nx
            y = ny
        # 뒤가 바다라면
        else:
            break
        turn_time = 0

print(count)

