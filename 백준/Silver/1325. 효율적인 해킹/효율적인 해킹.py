import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().strip().split())
graph = [[] for _ in range(N+1)] # 인접리스트(역방향)

for _ in range(M):
    A,B = map(int, input().strip().split())
    graph[B].append(A) # 연결관계 표현
    
# 함수 정의
def bfs(start_node):
    visited = [False] * (N + 1)
    queue = deque([start_node])
    
    visited[start_node] = True
    cnt = 1
    while queue:
        current_node = queue.popleft()
        
        for next_node in graph[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                cnt += 1
                
    return cnt
    
# 함수 실행
max_cnt = 0
result = []
for node_num in range(1, N+1):
    cnt = bfs(node_num)
    
    if cnt > max_cnt:
        max_cnt = cnt
        result = [node_num]
    elif cnt == max_cnt:
        result.append(node_num)
    
# 결과 출력
print(' '.join(map(str, result)))