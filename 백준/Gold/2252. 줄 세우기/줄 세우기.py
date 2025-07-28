import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())

in_degree = [0] * (N + 1) # 진입차수(0인덱스는 더미)
graph = [[] for _ in range(N + 1)] # N명의 학생에 대해 그래프 표현(0인덱스는 더미)
for _ in range(M):
    a, b = map(int, input().strip().split())
    graph[a].append(b) # 방향 표현(A -> B)
    in_degree[b] += 1
    
def topology_sort(graph, in_degree):
    queue = deque([i for i in range(1, N+1) if in_degree[i] == 0]) # 진입차수가 0인 학생들로 초기화
    sorted_result = []
    
    while queue:
        student = queue.popleft()
        
        sorted_result.append(student)
        for other_student in graph[student]:
            in_degree[other_student] -= 1
            
            if in_degree[other_student] == 0:
                queue.append(other_student)
                
    return sorted_result

result = topology_sort(graph, in_degree)
print(' '.join(map(str, result)))