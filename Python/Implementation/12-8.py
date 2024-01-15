s = input()
sum = 0
arr = []

for data in s:
  # 알파벳이면 리스트에 추가
  if data.isalpha():
    arr.append(data)
  else:
    # 숫자는 따로 덧셈
    sum += int(data)
# 문자는 정렬
arr.sort()
# 합계가 0이 아니면 맨 뒤에 삽입
if sum != 0:
  arr.append(str(sum))

print(''.join(arr))