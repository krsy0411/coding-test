import sys
input = sys.stdin.readline

N = int(input().strip())
# dp[i] = j : 정수 i에 대해 연산 최소 횟수
dp = [0] * (N + 1)
dp[1] = 0 # 1에서는 더 연산할 게 없음

for num in range(2, N + 1):
    dp[num] = dp[num - 1] + 1
    
    if num % 2 == 0:
        dp[num] = min(dp[num], dp[num // 2] + 1)
    if num % 3 == 0:
        dp[num] = min(dp[num], dp[num // 3]+ 1)
            
print(dp[N])