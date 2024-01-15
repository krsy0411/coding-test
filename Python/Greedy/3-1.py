n = 1260
cnt = 0

typeOfMoney = [500, 100, 50, 10]

for coin in typeOfMoney:
  cnt += n // coin
  # 나머지
  n %= coin

print(cnt)