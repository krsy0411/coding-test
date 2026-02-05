import sys
input = sys.stdin.readline

N,M = map(int, input().split())
S = [input().strip() for _ in range(N)]

result = []
distance = 0

for col in range(M):
    cnt = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
    }
    
    for row in range(N):
        cnt[S[row][col]] += 1
    
    # 각 열에서 가장 많이 등장한 문자 찾기(동률일 경우 사전순)
    max_char = min([c for c in cnt if cnt[c] == max(cnt.values())])
    result.append(max_char)
    distance += (N - cnt[max_char])
    
print(''.join(result))
print(distance)