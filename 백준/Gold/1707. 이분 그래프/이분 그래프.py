# 백준 1707 : 이분 그래프(너비우선탐색)
import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())

def bfs(graph, group, node):
    queue = deque([node])
    group[node] = 0
    
    while queue:
        current_node = queue.popleft()
        
        for neighbor_node in graph[current_node]:
            if group[neighbor_node] is None:
                group[neighbor_node] = 1 - group[current_node]
                queue.append(neighbor_node)
            elif group[neighbor_node] == group[current_node]:
                return False

    # 이분 그래프인 경우
    return True
        

# 테스트 케이스만큼 반복
for _ in range(T):
    V,E = map(int, input().strip().split())
    graph = [[] for _ in range(V + 1)]
    group = [None] * (V + 1)
    
    for _ in range(E):
        u,v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u)
    
    is_bipartite = True
    for vertex in range(1, V+1):
        if group[vertex] is None:
            if not bfs(graph, group, vertex):
                is_bipartite = False
                break
    
    print('YES' if is_bipartite else 'NO')