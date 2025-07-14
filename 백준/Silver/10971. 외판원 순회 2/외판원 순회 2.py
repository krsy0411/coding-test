import sys
input = sys.stdin.readline

N = int(input().strip())
map = [list(map(int, input().strip().split())) for _ in range(N)]

visited = [0] * N # N까지의 도시 방문 여부
result = float('inf')

def solve(start, now, depth, cost):    
    global visited
    global result
    
    if depth == N:
        if map[now][start] != 0:
            result = min(result, cost + map[now][start])
        return
    
    for next in range(N):
        if visited[next] == False and map[now][next] != 0:
            visited[next] = True
            solve(start, next, depth+1, cost + map[now][next]) # 재귀함수 호출
            visited[next] = False

for start in range(N):
    visited[start] = True
    solve(start, start, 1, 0) # 함수 실행 시작
    visited[start] = False
    
sys.stdout.write(str(result) + '\n')