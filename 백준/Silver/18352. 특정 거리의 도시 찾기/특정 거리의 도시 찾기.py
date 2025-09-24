import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# N : 도시의 개수, M : 도로의 개수, K : 거리 정보, X : 출발 도시 번호
N, M, K, X = map(int, input().strip().split())
graph = [[] for _ in range(N + 1)] # 인접 리스트
visited = [False] * (N + 1)

for _ in range(M):
    A, B = map(int, input().strip().split())
    graph[A].append(B) # 단방향 도로(무가중치)

result = [] # 최단거리가 K인 도시들(= 답)
def bfs(start):
    queue = deque([(start, 0)]) # (현재 도시, 현재까지 거리)
    
    visited[start] = True # 시작도시(X) 방문처리
    while queue:
        node, dist = queue.popleft()
        
        if dist == K:
            result.append(node)
            continue
        
        # 현재 도시에서 갈 수 있는 도시들 탐색
        for next_node in graph[node]:
            # 방문하지 않은 도시라면, 큐에 추가하고 방문처리
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, dist + 1))
                
bfs(X)
if result:
    result.sort()
    sys.stdout.write('\n'.join(map(str, result)))
else:
    sys.stdout.write('-1')