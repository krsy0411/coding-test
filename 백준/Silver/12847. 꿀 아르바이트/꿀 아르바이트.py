import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())
T = list(map(int, input().strip().split()))

current_sum = sum(T[:m])
result = current_sum
for i in range(m, n):
    current_sum += T[i] - T[i - m]
    result = max(result, current_sum)

print(result)