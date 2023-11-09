#  2중 반복문 구조
# 변수
n, m = map(int, input().split())
result = 0

# 입력
for row in range(n):
  data = list(map(int, input().split()))
  min_num = 10000
  # 현재 행에서 가장 작은 수 찾기
  for column in data:
    min_num = min(min_num, column)
  # 가장 작은 수들 중에서 가장 큰 수 찾기
  result = max(result, min_num)

# 출력
print(result)