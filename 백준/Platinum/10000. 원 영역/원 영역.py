# 백준 10000 : 원 영역
import sys
from bisect import bisect_left
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 해제
input = sys.stdin.readline

N = int(input().strip())
circles = []
for _ in range(N):
    x, r = map(int, input().strip().split())
    circles.append((x-r, x+r))
circles.sort(key=lambda x: (x[0], -x[1]))

count = 1 # 바깥영역 있으므로 1로 초기화
# 추가로 만들어지는 원의 영역 개수를 계산하는 함수
def recursive_solve(current_circle_idx, next_circle_idx):
    global count

    # 끝점이 동일한 경우
    if circles[current_circle_idx][1] == circles[next_circle_idx][1]:
        count += 1
        return
    
    # 끝점이 다른 경우 : 다음 끝점을 시작점으로 갖는 다른 원이 있는지 확인하고, 있으면 재귀호출
    temp_circle_idx = bisect_left(circles, (circles[next_circle_idx][1], ))
    if temp_circle_idx == len(circles):
        return
    if circles[temp_circle_idx][0] == circles[next_circle_idx][1]:
        recursive_solve(current_circle_idx, temp_circle_idx)
    # 없으면 그대로 종료

for i in range(N-1):
    # 왼쪽이 겹치면, 재귀로 오른쪽이 겹쳐지는 원이 나올때까지 재귀
    if circles[i][0] == circles[i+1][0]:
        recursive_solve(i,i+1)

print(N + count) 