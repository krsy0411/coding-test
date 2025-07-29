import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip()) # 완제품 번호
M = int(input().strip()) # 특정 부품을 완성하는 데 필요한 부품들 간의 관계 개수

graph = [[] for _ in range(N + 1)] # 인접리스트 방식
in_degree = [0] * (N + 1)
needs = [[0] * (N + 1) for _ in range(N + 1)] # N x N 크기의 2차원 배열 : 인덱스0은 더미
for _ in range(M):
    X, Y, K = map(int, input().strip().split())
    graph[Y].append((X,K))
    in_degree[X] += 1

def bfs_topology(graph, in_degree, needs):
    queue = deque([i for i in range(N + 1) if in_degree[i] == 0])

    while queue:
        num = queue.popleft()
        
        for neighbor_num, k in graph[num]:
            # num이 기본부품인 경우
            if sum(needs[num]) == 0:
                needs[neighbor_num][num] += k
            else:
                # 기본부품이 아닌 경우
                for i in range(1, N+1):
                    needs[neighbor_num][i] += needs[num][i] * k

            in_degree[neighbor_num] -= 1
            if in_degree[neighbor_num] == 0:
                queue.append(neighbor_num)
                    
bfs_topology(graph, in_degree, needs)
for i in range(1, N+1):
    if needs[N][i] > 0:
        print(f"{i} {needs[N][i]}")