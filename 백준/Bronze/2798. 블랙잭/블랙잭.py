import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))

result = 0 # 결과 : M과 가장 가까운 수
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            num1, num2, num3 = nums[i], nums[j], nums[k]
            
            if num1 + num2 + num3 <= M:
                result = max(result, num1 + num2 + num3)

print(result)