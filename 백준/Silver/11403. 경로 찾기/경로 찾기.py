import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().strip().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)] # 결과 : 2차원 리스트

def bfs(start, visited):
    queue = deque([start])
    visited[start] = True # 시작노드 방문처리
    
    while queue:
        node = queue.popleft()
        
        for next_node in range(N):
            if (graph[node][next_node] == 1) and (not visited[next_node]):
                visited[next_node] = True
                result[start][next_node] = 1 # 경로 존재
                queue.append(next_node)
            elif (graph[node][next_node] == 1) and (visited[next_node]):
                result[start][next_node] = 1 # 경로 존재
                
# 모든 노드에 대해 bfs 수행
for i in range(N):
    visited = [False] * N
    bfs(i, visited)
    
for row in result:
    sys.stdout.write(' '.join(map(str, row)) + '\n')