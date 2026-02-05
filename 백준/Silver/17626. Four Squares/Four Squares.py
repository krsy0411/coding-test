import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1) # dp[n] = n을 제곱수들의 합으로 나타낼 때 최소 개수

for n in range(1, N+1):
    dp[n] = n # 우선 최악의 경우로 초기화
    
    i = 1
    while i*i <= n:
        dp[n] = min(dp[n], dp[n - i*i] + 1)
        i += 1

# 결과 출력
print(dp[N])