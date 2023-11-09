# 첫째 줄
n,m = map(int,input().split())
# m개의 가로 갯수 : n번만큼 반복 : 맵 데이터 초기화 : 리스트 컴프리헨션 : 2차원 리스트 선언
data = [[0] * m for _ in range(n)]

# 둘째 줄
x,y,direction = map(int,input().split())
# 현재 위치도 방문처리
data[x][y] = 1

# 셋째 줄 : 데이터 처리는 항상 리스트로 편리하게 다루기
map_info = []
for i in range(n):
  map_info.append(list(map(int,input().split())))

# 북동남서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global direction
  # 반시계 방향 회전 : -1
  direction -= 1
  if direction == -1:
    direction = 3

count = 1
turn_time = 0

# 동작 수행
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 후, 가보지 않은 칸이 존재한다면 이동
  if data[nx][ny] == 0 and map_info[nx][ny] == 0:
    data[nx][ny] = 1
    x = nx
    y = ny
    # 이동횟수 증가
    count += 1
    # 회전을 더 안해도 되므로 다시 0으로 초기화
    turn_time = 0
    continue
  # 회전 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    # 더 회전을 해본다
    turn_time += 1
  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    # 한 칸 뒤로
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 이동할 수 있으면 뒤로 이동
    if map_info[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤로도 이동 불가능한 경우 : 반복문 탈출
    else:
      break
    turn_time = 0

print(count)