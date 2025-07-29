import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n+1)] # 인접리스트 방식(인덱스 0은 더미)
reversed_graph = [[] for _ in range(n+1)] # 인접리스트 방식(인덱스 0은 더미)
in_degree = [0] * (n+1) # 진입차수(인덱스 0은 더미)
dp = [0] * (n+1)

for _ in range(m):
    u,v,w = map(int, input().strip().split())
    graph[u].append((v,w)) # 정방향
    reversed_graph[v].append((u,w)) # 역방향
    in_degree[v] += 1 # v(도착노드)의 진입차수 증가

start, end = map(int, input().strip().split())

def find_longest_path():
    queue = deque([start])
    
    while queue:
        current_city = queue.popleft()
        
        for next_city, weight in graph[current_city]:
            dp[next_city] = max(dp[next_city], dp[current_city] + weight)
        
            in_degree[next_city] -= 1
            if in_degree[next_city] == 0:
                queue.append(next_city)
            
def reverse_count():
    count = 0
    visited = [False] * (n + 1)
    queue = deque([end])
    
    visited[end] = True
    while queue:
        current_city = queue.popleft()
        
        for prev_city, weight in reversed_graph[current_city]:
            if dp[current_city] == dp[prev_city] + weight:
                count += 1
                
                if not visited[prev_city]:
                    visited[prev_city] = True
                    queue.append(prev_city)
                
    return count

find_longest_path()
print(dp[end])
print(reverse_count())