# 백준 2253 : 점프
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())
# 못 밟는 돌의 번호
small_stones = set([int(input().strip()) for _ in range(M)])

visited = set()

queue = deque()
queue.append((1, 0, 0)) # (현재 돌 번호, 이전 점프 거리, 점프 횟수)
visited.add((1,0))

result = -1
while queue:
    current_stone, prev_jump, jump_count = queue.popleft()
    
    if current_stone == N:
        result = jump_count
        break
    
    for next_jump in [prev_jump - 1, prev_jump, prev_jump + 1]:
        if next_jump < 1:
            continue
        
        next_stone = current_stone + next_jump
        if next_stone > N or next_stone in small_stones or (next_stone, next_jump) in visited:
            continue
        
        visited.add((next_stone, next_jump))
        queue.append((next_stone, next_jump, jump_count + 1))
        
        if next_stone == N:
            result = jump_count + 1
            break

print(result)