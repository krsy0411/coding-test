import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
parent = [i for i in range(N+1)] # 각 노드의 부모 노드 정보 저장 배열 : 우선 자기 자신으로 초기화
visited = [False] * (N + 1)
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, visited, parent, node):
    queue = deque([node])
    visited[node] = True
    
    while queue:
        current_node = queue.popleft()
        
        for neighbor_node in graph[current_node]:
            if not visited[neighbor_node]:
                # 방문처리하고 부모 노드로 설정
                visited[neighbor_node] = True
                parent[neighbor_node] = current_node
                queue.append(neighbor_node)
                
bfs(graph, visited, parent, 1)
for i in range(2, N+1):
    print(parent[i])