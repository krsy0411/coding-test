import sys

input = sys.stdin.readline
N, M = map(int, input().strip().split()) # N: 행렬 크기, M: 합을 구해야 하는 횟수
matrix = [list(map(int, input().strip().split())) for _ in range(N)] # N x N 행렬 입력받기

prefix_sum_matrix = [[0] * (N + 1) for _ in range(N + 1)] # (N+1) x (N+1) 크기의 prefix sum 행렬 초기화
for i in range(1, N + 1):
    for j in range(1, N + 1):
        # prefix sum 계산 : 현재 위치의 값 + 왼쪽 값 + 위쪽 값 - 대각선 왼쪽 위 값
        prefix_sum_matrix[i][j] = matrix[i-1][j-1] + prefix_sum_matrix[i-1][j] + prefix_sum_matrix[i][j-1] - prefix_sum_matrix[i-1][j-1]

# M개의 쿼리에 대해 결과 출력
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().strip().split())
    # 구간 합 계산 : 현재 위치의 prefix sum - 왼쪽 구간 - 위쪽 구간 + 대각선 왼쪽 위 구간
    result = prefix_sum_matrix[x2][y2] - prefix_sum_matrix[x1-1][y2] - prefix_sum_matrix[x2][y1-1] + prefix_sum_matrix[x1-1][y1-1]
    
    print(result)