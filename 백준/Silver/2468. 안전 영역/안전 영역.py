import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input().strip())
map = [list(map(int, input().strip().split())) for _ in range(N)]
result = 0 # 안전영역 최대 개수

MAX_HEIGHT = 0 # 원소의 최대 높이 정보
for row in range(N):
    max_line = max(map[row])
    MAX_HEIGHT = max(MAX_HEIGHT, max_line) # 맵 내 가장 큰 높이 정보로 갱신

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(height, visited, x, y):  
    visited[x][y] = 1  # 첫 진입 시 방문처리
    
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and ny >=0 and nx < N and ny < N:
            if map[nx][ny] > height and visited[nx][ny] == 0:
                dfs(height, visited, nx, ny)
            
# 원소의 최대 높이 정보들에 대해 모두 확인
for rain_height in range(MAX_HEIGHT+1):
    temp = 0 # 임시 안전영역 개수
    visited = [[0] * N for _ in range(N)] # 2차원 배열(방문 여부 확인을 위해)
    
    for i in range(N):
        for j in range(N):
            if map[i][j] > rain_height and visited[i][j] == 0:
                dfs(rain_height, visited, i, j)
                temp += 1
                
    result = max(result, temp)

# 결과 출력
sys.stdout.write(str(result) + '\n')