# 5-10과 달리 본 문제는 상하좌우를 탐색하여 닿는 방향으로 이동해가며 몇스텝 나아갔는지를 확인하는 문제
# 현 위치 (1,1), 미로의 출구 (n,m), 한번에 한칸씩 이동하여 1로만 이동가능

# 이것도 재귀 활용, 이전 문제는 재귀로 풀면서 전체 함수의 True 값이 한번 나오면 한 덩어리였기 때문에 밖에서 구현으로 for문을 돌려줬어야했는데 이문제는 모든 원소를 다 돌 필요 없이 함수 내에서 1을 만나면 바로 그 자리의 상하좌우를 살피고, 또 다음 1의 상하좌우를 살피는 방식으로 재귀적으로 끝까지(n,m) 가서 카운트 수를 알아내면됨

n,m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

# 첫시작 0,0은 무조건 1이기 떄문에 그냥 바로 탐색 들어가도됨
# 함수에 좌표, 그래프까지 같이 받아야함. 그래프가 계속해서 업데이트 되기 때문
def escape_maze(x,y,maze):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny >=0 and ny <m :
            if maze[nx][ny] == 1 :
                maze[nx][ny] = maze[x][y] + 1
                escape_maze(nx,ny,maze)
    return maze[n-1][m-1]

print(escape_maze(0,0,maze))






