import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

d_row = [0, 0, -1, 1]
d_col = [-1, 1, 0, 0]

def bfs(row, col):
    queue = deque([(row, col)])
    
    visited[row][col] = True
    count = 1
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr, nc = r + d_row[i], c + d_col[i]
            
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and graph[nr][nc] == 1:
                visited[nr][nc] = True
                queue.append((nr, nc))
                count += 1
                
    return count

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i,j))
            
result.sort()
print(len(result))
print('\n'.join(map(str, result)))