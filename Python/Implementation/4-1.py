n = int(input())
plans = input().split()
# 초기 위치 설정
x,y = 1,1
# 인덱싱을 이용해서 위치 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
move_types = ['L', 'R', 'U', 'D']

# 이동계획 확인해서 위치 이동
for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나면 nx,ny를 x,y로 업데이트하지 않고 반복문으로 돌아감
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 공간을 벗어나지 않으면 현재 위치 업데이트
  x, y = nx, ny

print(x,y)