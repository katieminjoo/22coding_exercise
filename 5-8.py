# DFS 예제
# stack, recursive

def dfs(graph,v,visited):
    #현재 노드 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 현 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        # 1과 연결된 노드는 2,3,8이 있어
        # 2를 보자
        if visited[i] == False:
            # 2가 방문된적없다면 방문처리를 하고 다시 2에 연결된 다른 노드 방문 --> 재귀적으로 처리
            dfs(graph, i, visited)

graph = [[],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]]
visited = [False] * 9

dfs(graph, 1, visited)
# print(visited)
        