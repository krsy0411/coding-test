import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())

graph = [[] for _ in range(N + 1)]
for _ in range(N-1):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    
parent_info = [-1] * (N + 1)
def recursive_search_parent_node(node, parent_info):
    for next_node in graph[node]:
        if parent_info[next_node] is -1:
            parent_info[next_node] = node
            recursive_search_parent_node(next_node, parent_info)
    
    return

recursive_search_parent_node(1, parent_info)
for i in range(2, N+1):
    print(parent_info[i])