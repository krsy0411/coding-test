import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))

# 누적합 배열
prefix_sum = [0] * (n + 1)

# 누적합 계산
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

result = 0
for i in range(n):
    # arr[i]와 그 뒤의 모든 원소들의 합을 곱함
    result += (arr[i] * (prefix_sum[n] - prefix_sum[i + 1]))

print(result)