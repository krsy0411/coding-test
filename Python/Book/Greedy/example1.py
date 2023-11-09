money_types = [500, 100, 50, 10]

count = 0
n = 1700

# Q) 거슬러 줘야할 돈이 n일때 거슬러 줘야 할 동전의 최소개수는?
for money in money_types :
  # 큰 화폐부터 나눠지는 만큼 카운트
  count += n//money
  # 거슬러 줘야할 돈을 화폐만큼 나누고 남은 나머지로
  n %= money

print(count)