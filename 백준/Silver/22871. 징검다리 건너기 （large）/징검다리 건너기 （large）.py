import sys
input = sys.stdin.readline

# 입력
N = int(input())
A = list(map(int, input().split()))
            
INF = 10**18
dp = [INF] * N
dp[0] = 0

# i까지의 비용 계산(최대값들 중에서 최소)
for i in range(1, N):
    for j in range(i):
        this_time_jump_cost = (i - j) * (1 + abs(A[i] - A[j]))
        total_jump_cost = max(dp[j], this_time_jump_cost)
        # 값 갱신
        dp[i] = min(total_jump_cost, dp[i])
        
# 출력
sys.stdout.write(str(dp[N-1]))