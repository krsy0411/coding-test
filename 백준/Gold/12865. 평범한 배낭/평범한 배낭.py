import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().strip().split())
items = [tuple(map(int, input().strip().split())) for _ in range(N)]
dp = [[-1] * (K + 1) for _ in range(N + 1)]

def solve(i, w, dp):
    if i == 0 or w == 0:
        return 0
    
    if dp[i][w] != -1:
        return dp[i][w]
    
    weight, value = items[i - 1]
    if weight > w:
        dp[i][w] = solve(i - 1, w, dp)
    else:
        dp[i][w] = max(solve(i - 1, w, dp), solve(i - 1, w - weight, dp) + value)
        
    return dp[i][w]
    
# 결과 출력
print(solve(N, K, dp))