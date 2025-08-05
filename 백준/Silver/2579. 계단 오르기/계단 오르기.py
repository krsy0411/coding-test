import sys
input = sys.stdin.readline

N = int(input().strip())
stairs = [0] + [int(input().strip()) for _ in range(N)]

if N == 1:
    print(stairs[1])
elif N == 2:
    print(stairs[1] + stairs[2])
else:
    dp = [0] * (N + 1)
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, N+1):
        dp[i] = max(
                    dp[i-3] + stairs[i-1] + stairs[i],
                    dp[i-2] + stairs[i]
                )

    print(dp[N])