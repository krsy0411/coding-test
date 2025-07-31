# 백준 18405 : 경쟁적 전염
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().strip().split())
graph = [list(map(int,input().strip().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

d_row = [0, 0, -1, 1]
d_col = [-1, 1, 0, 0]                

S, X, Y = map(int, input().strip().split())
X -= 1
Y -= 1

start_virus = []
# 초기 바이러스 위치를 큐에 추가
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            start_virus.append((i, j, graph[i][j]))

start_virus.sort(key=lambda x: x[2])  # 바이러스 번호 순으로 정렬
queue = deque(start_virus)
while S > 0:
    size = len(queue)
    
    for _ in range(size):
        r, c, virus = queue.popleft()
        
        for i in range(4):
            nr = r + d_row[i]
            nc = c + d_col[i]
            
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and graph[nr][nc] == 0:
                visited[nr][nc] = True
                graph[nr][nc] = virus
                queue.append((nr, nc, virus))
                
    S -= 1
    
# 결과 출력
print(graph[X][Y])