import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().strip())) for _ in range(N)]
cost_graph = [[float('inf')] * N for _ in range(N)]

def dijsktra(graph, cost_graph):
    pq = [(0,0,0)] # 최소힙 기반 우선순위 큐 : (비용, 행, 열)
    cost_graph[0][0] = 0 # 시작 지점 비용 0으로 초기화
    
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]
    while pq:
        current_weight, current_row, current_col = heapq.heappop(pq)        

        if current_weight > cost_graph[current_row][current_col]:
            continue
        
        for i in range(4):
            n_row, n_col = d_row[i] + current_row, d_col[i] + current_col
            
            if 0 <= n_row < N and 0 <= n_col < N:        
                plus_weight = 0 if (graph[n_row][n_col] == 1) else 1 # 방 색깔에 따라 더해줄 값 결정
                next_weight = current_weight + plus_weight

                if next_weight < cost_graph[n_row][n_col]:
                    heapq.heappush(pq, (next_weight, n_row, n_col))
                    cost_graph[n_row][n_col] = next_weight

dijsktra(graph, cost_graph)
print(cost_graph[N-1][N-1])