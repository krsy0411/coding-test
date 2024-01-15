n = int(input())
# 데이터 처리를 위한 변수
data = []
# 결과값
result = 0
# 끝나는 시간 기준
standard = 0

# 둘째 줄
for i in range(n):
    data.append(list(map(int, input().split())))
# 시작 시간 기준 정렬
data.sort(key=lambda x : x[0])
# 끝나는 시간 기준 정렬 : 만약 정렬 도중 끝나는 시간이 동일하면, 시작시간 기준으로 이미 정렬됨(중요)
data.sort(key=lambda x : x[1])

for i, j in data:
    if i >= standard:
        standard = j
        result += 1

print(result)