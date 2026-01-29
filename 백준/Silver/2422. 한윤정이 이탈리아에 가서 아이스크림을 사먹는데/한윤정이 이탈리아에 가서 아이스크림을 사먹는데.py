import sys
input = sys.stdin.readline

N,M = map(int, input().strip().split())
bad_combis = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a,b = map(int, input().strip().split())
    bad_combis[a][b] = True
    bad_combis[b][a] = True

result = 0
# 안되는 조합인지 모든 경우 체크(브루트포스)
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if bad_combis[i][j]:
            continue
            
        for k in range(j+1, N+1):
            if bad_combis[i][k] or bad_combis[j][k]:
                continue
            result += 1 # 섞으면 안되는 조합이 아닌 경우
            
print(result)