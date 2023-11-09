n = int(input())
# 기본 정렬 라이브러리 이용
array = []
for i in range(n):
  array.append(int(input()))

# 내림차순 정렬
array.sort(reverse=True)

for i in array:
  print(i, end=" ")