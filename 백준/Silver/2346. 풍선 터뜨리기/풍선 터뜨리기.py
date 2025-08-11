import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

dq = deque(list((i+1, int(num)) for i,num in enumerate(input().strip().split()))) # 초기화
first_idx, first_value = dq.popleft()
last_value = first_value

print(first_idx, end=' ')
while dq:
    if last_value > 0:
        for i in range(last_value-1):
            dq.append(dq.popleft())
        idx, num = dq.popleft()
        last_value = num
        print(idx, end=' ')
    else:
        for i in range(abs(last_value)-1):
            dq.appendleft(dq.pop())
        idx, num = dq.pop()
        last_value = num
        print(idx, end=' ')