import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input().strip())
images = [list(map(int, list(input().strip()))) for _ in range(N)]
result = []

def quad_tree(x, y, n):
    color = images[x][y] # 기준 색
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 기준 색과 달라 압축이 안되는 경우, 4분할해서 다시 탐색
            if images[i][j] != color:
                result.append('(')
                quad_tree(x, y, n // 2) # 1사분면
                quad_tree(x, y + n // 2, n // 2) # 2사분면
                quad_tree(x + n // 2, y, n // 2) # 3사분면
                quad_tree(x + n // 2, y + n // 2, n // 2) # 4사분면
                result.append(')')
                return
    # 모두 같은 색이면, 압축한 값 추가
    result.append(str(color))
    
quad_tree(0, 0, N)
sys.stdout.write(''.join(result))