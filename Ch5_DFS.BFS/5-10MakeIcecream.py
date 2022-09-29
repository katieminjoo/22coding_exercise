# my code

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(int(input())))

result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 :
            # 방문표시를 하고 첫 시작점이 있음에 아이스크림 만든걸로 간주
            graph[i][j] = 1
            result += 1
            # 양옆상하를 보고 방문표시를 함
            # 오른쪽으로 끝까지 이동해가기
            # 0을 만나면 1로 바꾸고 한칸 이동
            # 0이 안나오거나 위치가 맵을 벗어나면 break
            while graph[i][j] == 0 and i < n :
                graph[i][j] = 1
                i += 1
            # 왼쪽으로
            while graph[i][j] == 0 and i >= 0 :
                graph[i][j] = 1
                i -= 1
            # 아래로
            while graph[i][j] == 0 and j < m:
                graph[i][j] = 1
                j += 1
            # 위로
            while graph[i][j] == 0 and j >= 0:
                graph[i][j] = 1
                j -= 1

print(result)
