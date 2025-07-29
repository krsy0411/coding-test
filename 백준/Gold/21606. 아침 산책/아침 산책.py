import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip()) # 정점 개수
A = [0] + list(map(int, input().strip()))
count = 0 # 가능한 서로 다른 산책 경로의 수

graph = [[] for _ in range(N + 1)]
for _ in range(N-1):
    u,v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u) # 무방향 그래프

def dfs(graph, arr, node, visited):
    global count

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if arr[neighbor] == 0:
                visited[node] = True
                dfs(graph, arr, neighbor, visited) # 인접노드가 실외인 경우
            else:
                visited[node] = True
                count += 1 # 인접노드가 실내인 경우

for i in range(1, N+1):
    visited = [False] * (N + 1)
    
    # 실내 시작만 고려
    if A[i] != 0:
        dfs(graph, A, i, visited)

print(count)