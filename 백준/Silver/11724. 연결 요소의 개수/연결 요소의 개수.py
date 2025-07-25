import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().strip().split())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node, visited, graph):
    visited[node] = True
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)
            
count = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, visited, graph)
        count += 1
        
print(count)