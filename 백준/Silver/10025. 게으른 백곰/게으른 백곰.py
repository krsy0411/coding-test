import sys
input = sys.stdin.readline

N,K = map(int, input().strip().split())
MAX_SIZE = 10**6
WINDOW_SIZE = 2 * K + 1
arr = [0] * (MAX_SIZE + 1)
for _ in range(N):
    gi, xi = map(int, input().strip().split())
    arr[xi] = gi # xi 위치에 gi 무게의 양동이 배치

current_sum = sum(arr[:WINDOW_SIZE])
result = current_sum
for i in range(WINDOW_SIZE, MAX_SIZE + 1):
    current_sum += arr[i] - arr[i - WINDOW_SIZE] # 슬라이딩 윈도우 방식으로 K 위치를 넘어가는 무게 계산
    result = max(result, current_sum)

print(result)