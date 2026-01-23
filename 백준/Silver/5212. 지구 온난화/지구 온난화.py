import sys
input = sys.stdin.readline

R,C = map(int, input().strip().split())

matrix = []
for _ in range(R):
    matrix.append([c for c in input().strip()])
    
new_matrix = [row[:] for row in matrix]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 시뮬레이션 : 잠길 지역 표시하기
for row in range(R):
    for col in range(C):
        if matrix[row][col] == '.':
            continue
        
        cnt = 0
        for k in range(4):
            nr = row + dr[k]
            nc = col + dc[k]
    
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                cnt += 1
            elif matrix[nr][nc] == '.':
                cnt += 1
        
        # 주변 바다 개수가 3 또는 4이면, 바다로 변할 예정
        if cnt == 3 or cnt == 4:
            new_matrix[row][col] = '.'
            
# 최소 사이즈 찾기
min_r, max_r = R, 0
min_c, max_c = C, 0
for i in range(R):
    for j in range(C):
        if new_matrix[i][j] == 'X':
            min_r = min(min_r, i)
            max_r = max(max_r, i)
            min_c = min(min_c, j)
            max_c = max(max_c, j)

# 출력
for i in range(min_r, max_r + 1):
    print(''.join(new_matrix[i][min_c:max_c+1]))