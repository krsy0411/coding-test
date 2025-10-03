import sys
from collections import deque

input = sys.stdin.readline

computer_nums = int(input().strip())
pairs_num = int(input().strip())

graph = [[] for _ in range(computer_nums+ 1)]
for _ in range(pairs_num):
    a, b = map(int, input().strip().split())
    
    graph[a].append(b)
    graph[b].append(a)

result = 0
visited = [False for _ in range(computer_nums + 1)]
def virus_search(node, answer):
    queue = deque([]) # 큐 초기화
    queue.append(node) # 초기 노드를 힙에 추가
    visited[node] = True
    
    while queue:
        pop_node = queue.popleft()
        
        for next_node in graph[pop_node]:
            if visited[next_node] == False:
                visited[next_node] = True
                queue.append(next_node)
                answer += 1
    
    return answer

result = virus_search(1, 0)
sys.stdout.write(f"{result}")