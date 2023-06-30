# 계수 정렬 방법
n = int(input())
arr = [0] * 1000001
# 가게에 있는 부품 번호를 기록
for i in input().split():
  arr[int(i)] = 1

# 손님이 요청한 부품 확인
m = int(input())
required_list = list(map(int, input().split()))

# 부품 확인하기 위한 반복문
for i in required_list:
  # 존재 여부 확인
  if i in arr:
    print('yes', end=' ')
  else:
    print('no', end=' ')