n, m, k = map(int, input().split())
# 리스트 안에 넣어서 데이터를 쉽게 처리하도록
data = list(map(int, input().split()))
# 오름차순 정렬
data.sort()
# 가장 큰 값
max_num = data[n-1]
# 두번째로 큰 값
second_num = data[n-2]

# 합산 결과
result = 0

# 결과 만들기
while True:
  # k번만큼 가장 큰 수를 반복 덧셈
  for i in range(k):
    if m == 0:
      break
    result += max_num
    m -= 1
  if m == 0 :
    break
  #  두번째로 큰 수는 한 번만 더해주는 용도
  result += second_num
  m-= 1

print(result)