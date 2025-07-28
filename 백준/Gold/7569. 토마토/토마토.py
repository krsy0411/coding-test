# 백준 7569 : 토마토
import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().strip().split())
d_row = [1,-1,0,0,0,0]
d_col = [0,0,1,-1,0,0]
d_height = [0,0,0,0,1,-1]

tomatoes = [[] for _ in range(H)]
for h in range(H):
    for _ in range(N):
        tomatoes[h].append(list(map(int, input().strip().split())))

# start_node : (높이, 행, 열, 날짜)
def bfs(tomatoes):
    result = -1
    queue = deque([])
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if tomatoes[h][r][c] == 1:
                    queue.append((h,r,c,0))
    
    while queue:
        h, n, m, day = queue.popleft()
        result = max(result, day)
        
        for i in range(6):
            n_row, n_col, n_height = (d_row[i] + n), (d_col[i] + m), (d_height[i] + h)
            
            if 0 <= n_row < N and 0 <= n_col < M and 0 <= n_height < H and tomatoes[n_height][n_row][n_col] == 0:
                queue.append((n_height, n_row, n_col, day + 1))
                tomatoes[n_height][n_row][n_col] = 1
                
    return result

result = bfs(tomatoes)
for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomatoes[h][r][c] == 0:
                print(-1)
                sys.exit()
            
print(result)