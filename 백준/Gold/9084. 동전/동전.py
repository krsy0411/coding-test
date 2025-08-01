import sys
input = sys.stdin.readline

def count(coins, m):
    dp = [0] * (m + 1)
    dp[0] = 1
    
    for coin in coins:
        # 점화식..
        for j in range(coin, m + 1):
            dp[j] += dp[j - coin]
            
    return dp[m]

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    coins = list(map(int, input().strip().split()))
    m = int(input().strip())
    
    print(count(coins, m))