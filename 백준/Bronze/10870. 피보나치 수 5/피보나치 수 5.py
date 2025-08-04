import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
dp = [0] * (N + 1)

def fibonacci(n):
    if n <= 1:
        return n
    
    dp[n] = fibonacci(n-1) + fibonacci(n-2)
    return dp[n]

result = fibonacci(N)
print(result)