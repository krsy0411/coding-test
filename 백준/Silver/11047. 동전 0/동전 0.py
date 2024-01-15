n, k = map(int, input().split())
count = 0
list = []
for _ in range(n):
  list.append(int(input()))
# 최소값을 위해 내림차순 정렬 : O(N)
list.sort(reverse=True)

# 큰 수부터 차례대로 나눠본다
for i in range(len(list)):
  # 몫이 0인 경우
  if(k // list[i] == 0):
    continue
  # 몫이 0이 아닌 경우
  count += k // list[i]
  k = k % list[i]

print(count)