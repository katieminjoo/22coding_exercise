B = ['X.....>', '..v..X.', '.>..X..', 'A......']
# B = ['...Xv','AX..^','.XX..']
# B = ['...', '>.A']
B = [list(b) for b in B]

for l in B :
    for m in l:
        print(m,end=" ")
    print()

n = len(B)
m = [len(_b) for _b in B][0]

# 상하좌우 ^v<>
direction = ['^','v','<','>']
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# A 현재위치 저장
ax,ay = 0,0
for i in range(n):
    for j in range(m):
        if B[i][j] == 'A':
            ax,ay = i,j

# 못가는 길 반영하고 숫자로 바꾼 B 완성
for i in range(n):
    for j in range(m):
        for k in range(4):
            if B[i][j] == direction[k]:
                B[i][j] = 0
                nx = i + dx[k]
                ny = j + dy[k]
                while nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if B[nx][ny] in direction:
                        break
                    else:
                        B[nx][ny] = 0
                        nx += dx[k]
                        ny += dy[k]

for i in range(n):
    for j in range(m):
        if B[i][j] == '.':
            B[i][j] = 1
        else:
            B[i][j] = 0


for l in B :
    for m in l:
        print(m,end=" ")
    print()

# 탐색 시작
def recursive_maze(x,y,graph):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                recursive_maze(nx,ny,graph)
    return graph

result = recursive_maze(ax,ay,B)

print('result')
for l in result :
    for m in l:
        print(m,end=" ")
    print()
final = result[n-1][m-1]
if int(final) > 1 :
    print('True')

                










