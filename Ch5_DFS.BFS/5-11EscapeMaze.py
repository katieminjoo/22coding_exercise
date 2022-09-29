# my code
# 미로탈출 : 왼쪽위에서 오른쪽 아래로 가야함

# n*m 의 n,m을 공백으로 구분하여 입력받기
n,m = map(int,input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

# 상하좌우
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 탐색 시작
def recursive_maze(x,y,graph):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                recursive_maze(nx,ny,graph)
    return graph[n-1][m-1]

print(recursive_maze(0,0,graph))