import sys
input = sys.stdin.readline

N = int(input().strip())
ropes = [int(input().strip()) for _ in range(N)]
ropes.sort(reverse=True)

max_weight = -float('inf') # 물체의 최대 중량
for i, rope in enumerate(ropes):
    max_weight = max(max_weight, rope * (i + 1)) # 더 작은 무게를 감당 가능한 루프의 무게 * n개
    
print(max_weight)