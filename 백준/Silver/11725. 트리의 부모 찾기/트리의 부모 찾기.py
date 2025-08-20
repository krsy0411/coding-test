import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input().strip()) # 노드 개수
parent = [0] * (N+1)
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# 간선(연결관계) 설정
for _ in range(N-1):
    u,v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)
    
# DFS 수행
def recursive_search(graph, parent, visited, node):
    visited[node] = True
    
    for next_node in graph[node]:
        if not visited[next_node]:
            parent[next_node] = node
            recursive_search(graph, parent, visited, next_node)
            
# 결과 출력
recursive_search(graph, parent, visited, 1)
sys.stdout.write('\n'.join(map(str, parent[2:])) + '\n')