import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().strip().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().strip().split())
    graph[u].append((w, v)) # (가중치, 정점)
    graph[v].append((w, u))

def prim():
    result = 0 # 최소 스패닝 트리의 가중치 합
    visited = [False] * (V + 1)
    
    for start in range(1, V + 1):
        if not visited[start]:
            min_heap = [(0, start)]
            heapq.heappush(min_heap, (0, start))
            
            while min_heap:
                weight, u = heapq.heappop(min_heap)
                
                if visited[u]:
                    continue
                
                visited[u] = True
                result += weight
                for next_weight, next_vertex in graph[u]:
                    if not visited[next_vertex]:
                        heapq.heappush(min_heap, (next_weight, next_vertex))
    
    return result

print(prim())