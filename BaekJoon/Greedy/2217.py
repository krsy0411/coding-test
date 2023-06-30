n = int(input())
ropes = []
result = []
for _ in range(n):
# 각 로프의 최대 가능 중량 입력
  ropes.append(int(input()))
# 로프들 중 가장 적게 버티는 값이 기준
ropes.sort(reverse=True)
# 들 수 있는 최대 중량 구하기 : 최소 감당 무게 * 연결된 로프 개수 : n개까지 병렬연결 가능
for i in range(n):
  result.append(ropes[i] * (i+1))

print(max(result))