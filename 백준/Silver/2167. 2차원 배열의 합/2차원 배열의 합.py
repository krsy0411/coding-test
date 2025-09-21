import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
array = [list(map(int, input().strip().split())) for _ in range(n)] # 2차원 배열 입력받기

# 누적합 배열 생성
prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # (i, j)까지의 합 계산
        prefix_sum[i][j] = array[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

k = int(input().strip())
for _ in range(k):
    i, j, x, y = map(int, input().strip().split())
    
    # (i, j)에서 (x, y)까지의 합(구간합) 계산
    result = prefix_sum[x][y] - prefix_sum[i-1][y] - prefix_sum[x][j-1] + prefix_sum[i-1][j-1]
    print(result)