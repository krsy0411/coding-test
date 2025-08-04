import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().strip().split())

result = []
queue = deque([i for i in range(1, N+1)])
while queue:
    # 우선 K-1개만큼 큐에서 빼서 뒤로 다시 추가
    for _ in range(K-1):
        queue.append(queue.popleft())
    
    k_num = queue.popleft()
    result.append(k_num)
    
print('<' + ', '.join(map(str, result)) + '>')