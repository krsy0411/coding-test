n, m = map(int, input().split())
result = 0

# 2차원 리스트(배열) 이용
graph = []
for i in range(n):
    # 입력받은 한 줄을 리스트로 바꾸어 그래프에 추가
    graph.append(list(map(int, input())))

# 좌표 이용 : True일 경우 방문처리, False일 경우 방문X
def dfs(x,y):
    # 좌표를 벗어나는 경우
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1
        # dfs : 스택 자료구조 : 재귀함수 이용
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    # 어느 경우에도 안 들어가면
    return False

# 동작 수행
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)