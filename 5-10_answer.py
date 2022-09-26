n,m = map(int,input().split())
graph = []
for _ in range(n):
    row=list(map(int,input()))
    graph.append(row)

# print(rows)
# v = row
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x < 0 or x >= n or y < 0 or y >= m :
        return False
    # 현재 노드를 아직 방문하지 않았다면
    # graph 상 0인 위치에서 연결된 노드 전부찾기
    if graph[x][y] == 0:
        # 방문으로 표시
        graph[x][y] = 1
        # 상,하,좌,우 위치도 모두 재귀적 호출
        # 방문으로 표시하기위한 작업
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        # 연결된 모든 노드를 찾으며 1로 변경하고 True를 리턴하며 아이스크림 한개 완성
        return True
    else:
        return False
    
# 모든 노드에 대하여 탐색
result = 0
for i in range(n):
    for j in range(m):
        # dfs를 수행하면 재귀적으로 인접노드들까지 dfs를 수행하지만 result에 반영되는 것은 인접노드방문 전 맨 처음 노드의 개수이다. 
        if dfs(i,j) == True:
            result += 1

print(result)