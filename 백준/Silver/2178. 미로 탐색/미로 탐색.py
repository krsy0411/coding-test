import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

def bfs(row,col):
    queue = deque([(row, col)])
    visited = [[False] * M for _ in range(N)]
    
    visited[row][col] = True
    d_row = [0, 0, -1, 1]
    d_col = [-1, 1, 0, 0]
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr, nc = r + d_row[i], c + d_col[i]
            
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maze[nr][nc] == 1:
                visited[nr][nc] = True
                maze[nr][nc] = maze[r][c] + 1
                queue.append((nr, nc))
                
    return maze[N-1][M-1]
  
result = bfs(0, 0)
print(result)