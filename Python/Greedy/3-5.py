n, k = map(int, input().split())
result = 0

# n >= k일때 : 나누기 먼저
while n >= k:
  # 만약 k로 나누어 떨어지지 않는다면 n에서 1씩 감소
  while (n % k != 0):
    n -= 1
    result += 1
  # 나누어 떨어지면
  n //= k
  result += 1

# 1 < n < k 인 경우 : 뺄셈
while (n > 1):
  n -= 1
  result += 1

print(result)