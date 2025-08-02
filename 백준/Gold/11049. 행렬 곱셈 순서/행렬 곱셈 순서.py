import sys
input = sys.stdin.readline

N = int(input().strip())

matrix = []
for _ in range(N):
    r, c = map(int, input().strip().split())
    matrix.append((r, c))
    
dp = [[0] * N for _ in range(N)]
for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = (
                dp[i][k] +
                dp[k + 1][j] +
                matrix[i][0] * matrix[k][1] * matrix[j][1]
            )
            dp[i][j] = min(dp[i][j], cost)
            
print(dp[0][N - 1])