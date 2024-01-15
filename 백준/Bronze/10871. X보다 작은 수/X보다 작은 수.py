n,x = map(int, input().split())
#리스트로 만들어서 인덱싱 이용
a = list(map(int, input().split()))

# a 원소 개수만큼 반복
for i in range(n):
    # 원소값이 x보다 작으면, 출력
    if a[i] < x:
        print(a[i], end=" ")