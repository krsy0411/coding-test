# 백준 3190 : 뱀
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())

graph = [[0] * N for _ in range(N)] # N x N 크기의 맵
for _ in range(K):
    x,y = map(int, input().strip().split())
    graph[x-1][y-1] = 2 # 2는 사과가 있음을 의미, 1은 뱀의 몸통이나 머리가 있음을 의미

L = int(input().strip())
turns = {} # 딕셔너리
for _ in range(L):
    num, direction = input().strip().split()
    turns[int(num)] = direction
    
second = 0 # 몇 초 걸렸는지 확인(결과)
queue = deque([(0,0)]) # 큐 생성 : 꼬리와 머리 좌표 보관용
graph[0][0] = 1

is_end = True # 게임 종료 알림용
move = [(0,1), (1,0), (0,-1), (-1,0)] # 시계방향
move_idx = 0 # 움직이는 방향에 대한 인덱스
while is_end:
    second += 1
    
    x, y = queue[-1] # 머리 현재 좌표
    dx, dy = move[move_idx]
    nx, ny = x + dx, y + dy
    # 충돌 확인 & 사과
    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != 1:
        # 사과가 아닌 경우에 : 꼬리는 제거
        if graph[nx][ny] != 2:
            tail_x, tail_y = queue.popleft()
            graph[tail_x][tail_y] = 0
        
        # 사과가 있든 없든 머리는 이동
        graph[nx][ny] = 1
        queue.append((nx,ny))
    else:
        # 벽이나 몸통에 충돌한 경우에는 게임 종료
        break
    
    # 방향전환
    if second in turns:
        if turns[second] == 'D':
            # 오른쪽 90도 회전
            move_idx = (move_idx + 1) % 4
        else:
            # 왼쪽 90도 회전
            move_idx = (move_idx + 3) % 4
    
# 결과 출력
print(second)