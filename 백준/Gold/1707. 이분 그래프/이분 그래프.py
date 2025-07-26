import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input().strip())

def dfs(graph, node, group):
    for neighbor_node in graph[node]:
        if group[neighbor_node] is None:
            group[neighbor_node] = 1 - group[node]
            
            if not dfs(graph, neighbor_node, group):
                return False
        elif group[neighbor_node] == group[node]:
            return False
    
    return True

for _ in range(T):
    V, E = map(int, input().strip().split())
    group = [None] * (V + 1)
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u,v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u) # 무방향 그래프
    
    is_bipartite = True
    for i in range(1, V+1):
        if group[i] is None:
            group[i] = 0
            
            if not dfs(graph, i, group):
                is_bipartite = False
                break
    
    # 결과 출력
    print('YES' if is_bipartite else 'NO')