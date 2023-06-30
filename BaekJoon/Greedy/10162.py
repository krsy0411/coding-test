t = int(input())
# a,b,c 순서 눌린 횟수 데이터 : 각각 300, 60 ,10 초
cnt = [0] * 3

# 우선, 10의 배수로 나누어 떨어지지 않으면 -1 출력
if t % 10 != 0:
  print(-1)
else:
  cnt[0] = t // 300
  cnt[1] = (t % 300) // 60
  cnt[2] = ((t % 300) % 60) // 10

  for i in range(len(cnt)):
    print(cnt[i],end=" ")