import sys
input = sys.stdin.readline

N,M = map(int, input().strip().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().strip().split())))

# 0~3 인덱스 : 위,우,아래,좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited = [[[False]*4 for _ in range(M)] for _ in range(N)]
wind = [[False]*M for _ in range(N)]

def search(x, y, d):
    cx, cy, cd = x, y, d
    
    while True:
        nx = cx + dx[cd]
        ny = cy + dy[cd]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            break
        
        if visited[nx][ny][cd]:
            break
        
        visited[nx][ny][cd] = True
        wind[nx][ny] = True
        
        current = matrix[nx][ny]
        if current == 1 and cd in (1,3):
            break
        elif current == 2 and cd in (0,2):
            break
        elif current == 3:
            cd = [1,0,3,2][cd]
        elif current == 4:
            cd = [3,2,1,0][cd]
            
        cx,cy = nx,ny
        
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 9:
            wind[i][j] = True
            
            for d in range(4):
                search(i,j,d)

result = 0
for i in range(N):
    for j in range(M):
        if wind[i][j] is True:
            result += 1
            
print(result)