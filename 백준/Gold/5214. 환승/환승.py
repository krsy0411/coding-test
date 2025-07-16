import sys
from collections import deque
input = sys.stdin.readline

N,K,M = map(int, input().split())
graph = [[] for _ in range(N + M + 1)]
for i in range(M):
    connections = list(map(int, input().split()))
    tube_station = N + 1 + i # 하이퍼튜브 인덱스 : N + 1부터 시작
    for station in connections:
        graph[tube_station].append(station)
        graph[station].append(tube_station)

def bfs(start):
    visited = [False] * (N + M + 1)
    queue = deque([(start, 1)])
    visited[start] = True
    
    while queue:
        current, depth = queue.popleft()
        
        if current == N:
            return depth
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                
                # 현재는 하이퍼튜브이고, 다음이 역인 경우(환승)
                if current > N and neighbor <= N:
                    queue.append((neighbor, depth + 1))
                else:
                    # 현재는 역이고, 다음이 하이퍼튜브인 경우(아직 카운트 하지 않음)
                    queue.append((neighbor, depth))
        
    return -1 # 도달할 수 없는 경우

print(bfs(1))