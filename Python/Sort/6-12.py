n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 올림차순, b는 내림차순으로 정렬해서 차례대로 값 비교
a.sort()
b.sort(reverse=True)
# k번만큼 바꿔치기 수행
for i in range(k):
  # 맨 앞 인덱스부터 차례대로 값 확인 : 이미 정렬되어 있으므로
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break
# a리스트 데이터들의 합산 결과 출력
print(sum(a))