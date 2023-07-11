# 입력
n, m = map(int, input().split())
weights = list(map(int, input().split()))
# 결과
result = 0

for now_i in range(len(weights)):
    if now_i == len(weights) - 1:
        break
    for next_i in range(now_i + 1, len(weights)):
        # 만약 무게가 같다면
        if weights[now_i] == weights[next_i]:
            continue
        # 만약 무게가 같지 않다면
        else:
            result += 1

print(result)
