# 백준 1916 : 최소비용 구하기
import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int, input().strip().split())
    graph[u].append((v,w)) # 방향 그래프

def dijkstra(graph, start):
    distance = [float('inf')] * (N + 1)
    pq = [(0, start)] # 최소힙

    distance[start] = 0 # 자기자신 초기화
    while pq:
        cost, city = heapq.heappop(pq)
        
        # 이미 거리가 더 짧으면 패스
        if distance[city] < cost:
            continue

        # 인접 노드 확인
        for neighbor, weight in graph[city]:
            next_cost = cost + weight
            # 더 짧은 경로가 발견되면
            if next_cost < distance[neighbor]:
                distance[neighbor] = next_cost
                heapq.heappush(pq, (next_cost, neighbor))
                
    return distance

start_city , destination_city = map(int, input().strip().split())
shortest_dist = dijkstra(graph, start_city)
print(shortest_dist[destination_city])