import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().strip().split())

heavy_direction_graph = [[] for _ in range(N + 1)]
light_direction_graph = [[] for _ in range(N + 1)]
for _ in range(M):
    heavy, light = map(int, input().strip().split())
    
    heavy_direction_graph[light].append(heavy)
    light_direction_graph[heavy].append(light)

def dfs(graph, node, visited):
    count = 0
    
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            count += 1
            count += dfs(graph, next_node, visited)
    
    return count

result = 0
for i in range(1, N+1):
    heavy_count = dfs(heavy_direction_graph, i, [False] * (N + 1))
    if heavy_count >= (N + 1) // 2:
        result += 1
        continue
    
    light_count = dfs(light_direction_graph, i, [False] * (N + 1))
    if light_count >= (N + 1) // 2:
        result += 1
        continue

print(result)