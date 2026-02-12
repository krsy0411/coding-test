import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

N,M = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 값이 2인 지점 찾기
start_x = 0
start_y = 0
for x in range(N):
    for y in range(M):
        if graph[x][y] == 2:
            queue.append((x,y))
            visited[x][y] = 0

# 모든 지점 탐색하며 출력할 값 갱신
while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == -1 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
            
# 결과 출력
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()