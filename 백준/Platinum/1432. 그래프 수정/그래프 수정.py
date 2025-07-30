# 백준 1432 : 그래프 수정
import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
out_degree = [0] * (N + 1) # 진출차수
result = [0] * (N + 1)

graph = [[] for _ in range(N + 1)] # 인접리스트 기반(인덱스 0은 더미)
for i in range(1, N + 1):
    line = list(map(int, input().strip()))
    
    for idx, val in enumerate(line):
        if val == 1:
            graph[idx + 1].append(i)
            out_degree[i] += 1
            
def topology_sort(n):
    heap = []
    
    for i in range(1, n+1):
        if out_degree[i] == 0:
            heapq.heappush(heap, -i) # 최대힙
            
    while heap:
        current = -(heapq.heappop(heap))
        result[current] = n
        
        for neighbor in graph[current]:
            out_degree[neighbor] -= 1
            
            if out_degree[neighbor] == 0:
                heapq.heappush(heap, -neighbor)
        
        n -= 1
        
topology_sort(N)
if result.count(0) > 2:
    print(-1)
else:
    print(' '.join(map(str, result[1:])))