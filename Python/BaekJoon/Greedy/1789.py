s = int(input())
cnt = 0
num = 1
while True:
  s -= num
  num += 1
  cnt += 1
  if s < num:
    break

print(cnt)