# 문자열S가 들어옴
s = input()
# 데이터 첫번째 값은 이미 결과로 들어가고 시작
result = int(s[0])

# 두번째 값부터 확인해가면서 덧셈 혹은 곱셈
for i in range(1, len(s)):
  data = int(s[i])
  # 첫 진입이라 결과가 1이하 && 2번째 이후 원소가 1이하 : 덧셈
  if result <= 1 or data <= 1:
    result += data
  # 나머지는 곱셈
  else:
    result *= data

print(result)