# DFS (Depth-First Search 깊이 우선 탐색)
# Node, Edge, Vertex
# 두 노드가 간선으로 연결되어 있다면 '두 노드는 인접하다' 

# 인접행렬방식으로 표현 Adjacency Matrix
# 연결이 없는 노드끼리는 무한의 비용으로 작성한다.
inf = 999999999 # 무한의 비용 선언
# 2차원 리스트를 이용
matrix_graph = [[0,7,5],[7,0,inf],[5,inf,0]]

print(matrix_graph)
# 인접리스트방식
# row가 3개인 2차원 리스트로 표현
graph = [[] for _ in range(3)]

#첫번째 노드 0에 연결된 노드 정보 저장(노드 & 거리)
graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)
