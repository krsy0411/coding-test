# 입력
n, k = map(int, input().split())
cnt = 0

# n이 k보다 크면 우선 나눠주기 - 최소 횟수
while True:
  # k로 나누어떨어지는 횟수 = (n // k)
  howManyTimeSubtraction = (n // k) * k
  # 1빼야하는 횟수만큼 카운트
  cnt = (n - howManyTimeSubtraction)
  # n은 k로 나누어떨어지는 수
  n = howManyTimeSubtraction
  
  # k보다 작은 경우
  if n < k:
    break
  
  # n = k로 나눴을때 몫
  n //= k
  cnt += 1

# while문 바깥 : n < k : 1씩 빼기
cnt += (n-1)
print(cnt)