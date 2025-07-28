# 백준 3055 : 탈출
import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().strip().split())
graph = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

d_row, d_col = [-1,1,0,0], [0,0,-1,1]
def bfs(graph, start, visited):
    time = 0
    animal_queue = deque([start]) # (행, 열, 시간)
    water_queue = deque([])
    for i in range(R):
        for j in range(C):
            if graph[i][j] == '*':
                water_queue.append((i,j)) # (행, 열) : 물 위치 초기화
    
    visited[start[0]][start[1]] = True
    while animal_queue:
        # 물 먼저 확장
        for _ in range(len(water_queue)):
            wr, wc = water_queue.popleft()
            
            for i in range(4):
                nwr, nwc = (wr + d_row[i]), (wc + d_col[i])
                
                if 0 <= nwr < R and 0 <= nwc < C and graph[nwr][nwc] == '.' and not visited[nwr][nwc]:
                    visited[nwr][nwc] = True
                    graph[nwr][nwc] = '*' # 물 영역 확장
                    water_queue.append((nwr,nwc)) # 물 큐에 다음 영역 추가
        
        # 고슴도치 이동
        for _ in range(len(animal_queue)):
            r,c,t = animal_queue.popleft()

            for i in range(4):
                n_row, n_col = (r + d_row[i]), (c + d_col[i])

                if 0 <= n_row < R and 0 <= n_col < C and not visited[n_row][n_col]:
                    if graph[n_row][n_col] == '.':
                        visited[n_row][n_col] = True # 방문처리
                        animal_queue.append((n_row, n_col, t+1))
                    elif graph[n_row][n_col] == 'D':
                        # 다음 위치가 비버굴이면 시간만 갱신하고 곧바로 반복문 탈출
                        time = t + 1
                        return time

    return time

result = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            result = bfs(graph, (i,j,0), visited)
            
print("KAKTUS" if (result == 0) else result)