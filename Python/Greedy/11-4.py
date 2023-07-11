# 입력
n = int(input())
# 데이터를 입력받아 올림차순 정렬
data = list(map(int, input().split()))
data.sort()

result = 1
# 처리 과정
for i in data:
    if (i > result):
        break
    result += i

print(result)
