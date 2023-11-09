n = int(input())
roads = list(map(int,input().split()))
prices = list(map(int,input().split()))

total_price = 0
# 첫 도시의 기름값으로 최소비용 초기화
min_cost = prices[0]
# 첫번째 주유소는 무조건 주유를 해야함
total_price += roads[0] * prices[0]
for i in range(1,n-1):
  # 만약 최소비용보다 더 적게 드는 비용
  if min_cost > prices[i]:
    min_cost = prices[i]

  total_price += min_cost * roads[i]

print(total_price)