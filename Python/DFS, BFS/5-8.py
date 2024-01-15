# 0 ~ 8번 노드에 연결된 정보 : 인접 행렬
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

# 그래프, 현재 노드, 방문처리
def dfs(graph, v, visited):
  # 현재 노드 방문처리
  visited[v] = True
  print(v, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문 : 작은 수의 노드를 앞에 배치해서 작은 수부터 확인
  for i in graph[v]:
    # 기준 : 방문하지 않았다면
    if not visited[i]:
      dfs(graph, i, visited)

dfs(graph, 1, visited)