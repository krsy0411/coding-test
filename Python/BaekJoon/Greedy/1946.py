t = int(input())

# 테스트 케이스만큼 반복
for _ in range(t):
  # n값 입력받기
  n = int(input())
  result = 0
  # n명만큼 (서류성적, 면접성적) 형태로 리스트 안에 저장
  applicant = [[int(x) for x in input().split()] for _ in range(n)]
  # 선별 기준 : 일단 우선 서류성적 순으로 정렬
  applicant.sort()
  # 일단 서류성적이 가장 좋은 사람
  best_rank = applicant[0][1]
  # 판별하고자 하는 지원자의 성적이 서류성적이 가장 좋은 사람보다 좋지 않으면 탈락
  for i in range(n):
    rank = applicant[i][1]
    if rank < best_rank:
      # 만약 판별하고자 하는 지원자의 성적이 더 좋다면 최상 성적을 업데이트 해준다
      best_rank = rank
      result += 1
  print(result)