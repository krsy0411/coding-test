import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())

graph = [[0] * N for _ in range(N)]
for _ in range(K):
	row, col = map(int, input().strip().split())
	graph[row-1][col-1] = 2 # 그래프 상의 2는 사과가 있음을 의미, 1은 뱀\

L = int(input().strip())
directions = {}
for _ in range(L):
	t, d = input().strip().split()
	directions[int(t)] = d

# 주요 로직 시작
queue = deque([(0,0)])
time = 0 # 결과

# 이동방향 : 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
move_idx = 0

while True:
	# 시간 증가
	time += 1
	
	# 현재와 다음 위치 좌표 계산
	current_row, current_col = queue[-1][0], queue[-1][1]
	next_row, next_col = queue[-1][0] + dx[move_idx], queue[-1][1] + dy[move_idx]
	
	if 0 <= next_row < N and 0 <= next_col < N and graph[next_row][next_col] != 1:
		# 사과가 존재하지 않는 경우 -> 꼬리도 움직임
		# 사과가 존재하는 경우 -> 머리만 움직임
		if graph[next_row][next_col] != 2:
			tail_row, tail_col = queue.popleft() # 꼬리 꺼내기
			graph[tail_row][tail_col] = 0
		
		queue.append((next_row, next_col)) # 머리 위치는 큐에 삽입
		graph[next_row][next_col] = 1
		
		# 방향 전환할 시간인지 확인하고 적용
		if time in directions:
			if directions[time] == 'L':
				move_idx = (move_idx - 1) % 4
			else:
				move_idx = (move_idx + 1) % 4
	else:
		break

# 결과 출력
print(time)