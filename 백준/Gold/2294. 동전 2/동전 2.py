import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().strip().split())

def bfs(nums, min_count, visited):
    queue = deque([(0,0)]) # (숫자, 동전 개수)

    while queue:
        n, cnt = queue.popleft()
        
        for num in nums:
            acc = n + num
            
            if acc > K or acc in visited:
                continue
            
            visited.add(acc)
            if acc == K:
                return min(min_count, cnt + 1)
            
            queue.append((acc, cnt + 1))
            
    return -1
        
visited = set()
nums = [int(input().strip()) for _ in range(N)] # 각 동전의 가치
min_count = bfs(nums, float('inf'), visited)
print(min_count)