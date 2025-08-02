# 백준 2098 : 외판원 순회
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

# dp[현재 도시][방문 상태] = 최소 비용
dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(current, visited):
    # 모든 도시를 방문했다면 → 출발 도시(0)으로 복귀
    if visited == (1 << N) - 1:
        return W[current][0] if W[current][0] > 0 else float('inf')
    
    if dp[current][visited] != -1:
        return dp[current][visited]
    
    min_cost = float('inf')
    for next_city in range(N):
        if visited & (1 << next_city):  # 이미 방문한 도시
            continue
        if W[current][next_city] == 0:  # 길 없음
            continue
        
        new_visited = visited | (1 << next_city)
        cost = W[current][next_city] + tsp(next_city, new_visited)
        min_cost = min(min_cost, cost)
    
    dp[current][visited] = min_cost
    return min_cost

print(tsp(0, 1 << 0))  # 도시 0에서 출발, 도시 0만 방문한 상태