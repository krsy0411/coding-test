import sys
input = sys.stdin.readline

n = int(input().strip())
dp = [0] * (n + 1)
dp[1] = 1

def fibonacci(n):
    if n == 0:
        return 0
    
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dp[n]

print(fibonacci(n))