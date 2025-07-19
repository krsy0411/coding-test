# 백준 18258 : 큐 2
from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())
queue = deque() # 큐 생성
for _ in range(N):
    command = input().strip().split()
    cmd = command[0]
    
    if cmd == 'push':
        queue.append(command[1])
    elif cmd == 'pop':
        print(queue.popleft() if queue else -1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        print(0 if queue else 1)
    elif cmd == 'front':
        print(queue[0] if queue else -1)
    else:
        print(queue[-1] if queue else -1)