import sys
input = sys.stdin.readline

N, M = map(int, input().split())
floor = [input().strip() for _ in range(N)]

count = 0
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        
        visited[i][j] = True
        
        # 바닥 장식이 '-'인 경우
        if floor[i][j] == '-':
            count += 1
            
            for k in range(j, M):
                if floor[i][k] == '-':
                    visited[i][k] = True
                else:
                    break
        
        # 바닥 장식이 '|'인 경우
        elif floor[i][j] == '|':
            count += 1
            
            for k in range(i, N):
                if floor[k][j] == '|':
                    visited[k][j] = True
                else:
                    break 

# 결과 출력
print(count)