import sys
from collections import deque
input = sys.stdin.readline

N,M,K,X = map(int, input().strip().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().strip().split())
    graph[A].append(B) # 단방향 도로

def bfs(graph, visited, node=X):
    queue = deque([(node,0)]) # (노드 번호, 거리)
    visited[node] = True # 시작 노드 방문 처리
    result = [] # 결과 처리용 배열

    while queue:
        current_node, current_dist = queue.popleft()

        if current_dist == K:
            result.append(current_node)
        
        for neighbor_node in graph[current_node]:
            if not visited[neighbor_node]:
                visited[neighbor_node] = True
                queue.append((neighbor_node, current_dist + 1))

    return sorted(result)

result = bfs(graph, visited, X)
if not result:
    print(-1)
else:
    for node in result:
        print(node)