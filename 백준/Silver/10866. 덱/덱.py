import sys
from collections import deque

input = sys.stdin.readline
N = int(input().strip())

dq = deque()
for i in range(N):
    line = input().strip().split()
    
    if line[0] == 'push_front':
        X = int(line[1])
        dq.appendleft(X)
        continue
    elif line[0] == 'push_back':
        X = int(line[1])
        dq.append(X)
        continue
    elif line[0] == 'pop_front':
        X = (dq.popleft() if dq else -1)
        print(X)
        continue
    elif line[0] == 'pop_back':
        X = (dq.pop() if dq else -1)
        print(X)
        continue
    elif line[0] == 'size':
        print(len(dq))
        continue
    elif line[0] == 'empty':
        print(0 if dq else 1)
        continue
    elif line[0] == 'front':
        print(dq[0] if dq else -1)
        continue
    elif line[0] == 'back':
        print(dq[-1] if dq else -1)
        continue