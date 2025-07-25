import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, V = map(int, input().strip().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)
    
dfs_result = []
visited_dfs = [False] * (N + 1)
def dfs(v, visited):
    visited[v] = True
    dfs_result.append(v)
    
    for neighbor in sorted(graph[v]):
        if not visited[neighbor]:
            dfs(neighbor, visited)
            
bfs_result = []
visited_bfs = [False] * (N + 1)
def bfs(v, visited):
    queue = deque([v])
    
    visited[v] = True
    while queue:
        current = queue.popleft()
        bfs_result.append(current)
        
        for neighbor in sorted(graph[current]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

dfs(V, visited_dfs)
bfs(V, visited_bfs)

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))