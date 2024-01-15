h = int(input())

count = 0
for hour in range(h+1):
  for min in range(60):
    for sec in range(60):
      # 시각을 문자열로 캐스팅
      if '3' in str(hour) + str(min) + str(min):
        count += 1

print(count)