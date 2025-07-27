import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip().split())))

d_row = [-1,1,0,0]
d_col = [0,0,-1,1]

# 한 덩이러 전체를 방문하고 처리하는 함수
def bfs(start, visited, graph):
    queue = deque([start])
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr, nc = r + d_row[i], c + d_col[i]
            
            if (0 <= nr < N) and (0 <= nc < M) and (not visited[nr][nc]) and (graph[nr][nc] != 0):
                # 방문처리, 큐에 인접노드 넣기
                visited[nr][nc] = True
                queue.append((nr, nc))

def melt(graph):
    new_graph = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                for k in range(4):
                    n_row, n_col = i + d_row[k], j + d_col[k]
                    if 0 <= n_row < N and 0 <= n_col < M and graph[n_row][n_col] == 0:
                        new_graph[i][j] += 1
    
    for i in range(N):
        for j in range(M):
            graph[i][j] = max(0, graph[i][j] - new_graph[i][j]) # 빙산 녹은 양만큼 기존 그래프에 적용
            
time = 0
while True:
    iceberg_count = 0
    visited = [[False] * M for _ in range(N)]
    
    # 덩어리 개수 세기 : 아직 방문 안 한 지점이 있으면 덩어리 개수를 증가시키고 인접한 칸들도 방문처리
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                iceberg_count += 1
                visited[i][j] = True
                bfs((i, j), visited, graph)
    
    # 만약 덩어리가 0개라면 종료
    if iceberg_count == 0:
        print(0)
        break
    elif iceberg_count > 1:
        print(time)
        break
    
    # 빙산 녹이기
    melt(graph)
    
    # 시간 증가
    time += 1