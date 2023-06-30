n = int(input())
fears = list(map(int, input().split()))
# 오름차순 정렬 : 그룹수 최대치 구하기
fears.sort()

result = 0
# 현재 그룹 인원 수
count = 0

for fear in fears:
  count += 1
  # 만약 현재 그룹 인원 수가 공포도와 같거나 더 많으면
  if count >= fear:
    # 총 그룹 수 증가
    result += 1
    # 현재 그룹 인원수 초기화
    count = 0

print(result)