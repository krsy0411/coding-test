price = int(input())
change = 1000 - price

types_of_money = [500, 100, 50, 10, 5, 1]
cnt = 0

for type in types_of_money:
  # 물건가격이 1000원이면 패스
  if change == 0:
    break
  cnt += change // type
  change = change % type

print(cnt)