from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]    

def bfs(x,y):
    queue = deque()
    # 튜플 형태
    queue.append((x,y))
    # 큐 자료구조는 재귀함수 형태로 사용할 수 없음
    while queue:
        # 튜플 형태 값을 각각 분리
        x,y = queue.popleft()
        # 재귀함수x 대신 반복문 : 큐 자료구조
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          # 좌표를 벗어나면 무시
          if nx < 0 or nx >= n or ny < 0 or ny >= m:
              continue
          # 괴물 구역이면 무시
          if graph[nx][ny] == 0:
              continue
          # 노드에 처음 방문하는 경우에만 최단거리 기록
          if graph[nx][ny] == 1:
              # 방문노드 값을 업데이트하여 방문처리
              graph[nx][ny] = graph[nx][ny] + 1
              queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))