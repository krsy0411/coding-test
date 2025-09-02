import sys
input = sys.stdin.readline

N = int(input().strip())
result = 0
for num in range(1, N+1):
    digit_sum = sum(map(int, str(num)))
    
    if num + digit_sum == N:
        result = num
        break

print(result)