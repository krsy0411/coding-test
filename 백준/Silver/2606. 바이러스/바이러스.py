import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (N + 1)
count = 0
def dfs(node, visited):
    global count
    
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += 1
            dfs(neighbor, visited)

dfs(1, visited)
print(count)