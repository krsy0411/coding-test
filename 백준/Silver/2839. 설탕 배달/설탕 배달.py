n = int(input())
cnt = 0

while(n >= 0):
  # 5로 나눠 떨어지는 경우: 최소 개수를 위함
  if (n % 5 == 0):
    cnt += (n//5)
    print(cnt)
    break
  #  5로 안 나눠 떨어지는 경우 : 3kg 봉지는 제일 적게 쓰여야함
  n -= 3
  cnt += 1

# while문을 깨고 나왔다 = 더 이상 나눠지지 않는다
if(n < 0):
  print(-1)