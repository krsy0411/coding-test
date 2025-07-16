import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
M = int(input().strip())
friends_list = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().strip().split())
    friends_list[a].append(b)
    friends_list[b].append(a)

def bfs(start):
    queue = deque([(start, 0)])
    visited = [False] * (N + 1)
    visited[start] = True
    count = 0

    while queue:
        current, current_depth = queue.popleft()

        if 1 <= current_depth <= 2:
            count += 1

        if current_depth > 2:
            continue

        for neighbor in friends_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, current_depth + 1))

    return count

result = bfs(1)
sys.stdout.write(str(result) + '\n')