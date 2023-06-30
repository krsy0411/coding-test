n = int(input())
m = int(input())
height_list = list(map(int, input().split()))
# 변수 설정
result = 0
# 이진탐색용 시작,끝점
start = 0
end = max(height_list)
result = 0

# 탐색 수행
while(start <= end):
  total = 0
  mid = (start + end) // 2
  # 반복 돌면서 잘린 떡 길이 총합 구해내기
  for height in height_list:
    # 중간값보다 길면 잘라내고 총합 갱신
    if height > mid:
      total += height - mid
    # 중간값보다 짧으면 무시
  # 총합 떡 양이 부족하면 더 길게 잘라내기
  if total < m:
    end = mid - 1
  # 총합 떡 양이 충분하면 더 짧게 잘라내기
  else:
    start = mid + 1
    # 결과값은 중간값이 된다
    result = mid


# 결과 출력
print(result)