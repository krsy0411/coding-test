n = int(input())
pi = list(map(int, input().split()))
total = 0
# 오름차순 정렬 : O(N)
pi.sort()

for i in range(n):
  pi[i] = pi[i] * (n-i)
  total += pi[i]

print(total)