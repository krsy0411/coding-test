n = int(input())

arr = []
for i in range(n):
  # 2번째 줄부터 입력되는 (이름, 점수) 데이터를 split해서 리스트로 만듦
  input_data = input().split()
  # 이름은 문자열 그대로, 점수는 정수형으로 반환해서 튜플 형태로 저장
  arr.append((input_data[0], int(input_data[1])))

# 점수를 기준으로 올림차순 정렬
arr.sort(key=lambda student: student[1])
# 결과를 이름으로 출력
for i in arr:
  print(i[0], end=' ')