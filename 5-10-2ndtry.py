# 이 문제는 상하좌우에 닿는 0값이 몇개인지가 아니라 그 덩어리가 몇개인지 찾는 문제
# n*m 크기의 얼음틀이 있다
n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

# Point
# 한 묶음을 찾으면 시작점 하나만 카운트 하면 되고, 묶음 내의 다른 숫자들은 1로 변경시켜주면 됨
# 상하좌우 살피는데, 맵 바깥으로 못나가가게 제한 걸기

# 재귀함수를 써보자 ( 연결된 부분을 만나면 그 위치에서 또 함수 실행 )
def connect(x,y):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    if x < 0 or x >= n or y <0 or y >= m:
        return False
    if graph[x][y] == 0 :
        # 1로 값을 바꾸어주고 한 묶음 찾은거 count에 반영
        graph[x][y] = 1
        # 상하좌우 0인지 확인
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            connect(nx,ny)
        return True

# 실행 부분
count = 0
for i in range(n):
    for j in range(m):
        if connect(i,j) == True:
            count += 1

print(count)


    


