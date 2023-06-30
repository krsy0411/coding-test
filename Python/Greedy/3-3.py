# 변수
result = 0

# 입력
n, m = map(int, input().split())
for row in range(n):
  # 여러 데이터의 효율적 처리를 위해 리스트 이용
  data = list(map(int, input().split()))
  min_num = min(data)
  # 룰을 따른 값들 중에서 가장 큰 수를 result에 담기
  result = max(result, min_num)

# 출력
print(result)