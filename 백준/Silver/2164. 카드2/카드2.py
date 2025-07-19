# 백준 2164 : 카드 2
from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())
queue = deque([i+1 for i in range(N)])

while queue:
    if len(queue) == 1:
        print(queue.popleft())
        break
    
    # 1. 맨 앞 숫자 버리기
    queue.popleft()
    # 2. 버린 숫자 직후의 숫자는 큐의 맨 뒤로 추가
    num = queue.popleft()
    queue.append(num)