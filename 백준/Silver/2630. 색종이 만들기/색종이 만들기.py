import sys
input = sys.stdin.readline

N = int(input().strip())
paper = [list(map(int, input().strip().split())) for _ in range(N)]

def recursive_count(x, y, size, counts):
    color = paper[x][y] # 현재 색종이의 색
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                recursive_count(x, y, size // 2, counts)  # 왼쪽 위
                recursive_count(x, y + size // 2, size // 2, counts) # 오른쪽 위
                recursive_count(x + size // 2, y, size // 2, counts) # 왼쪽 아래
                recursive_count(x + size // 2, y + size // 2, size // 2, counts) # 오른쪽 아래
                return
    
    if color == 0:
        counts[0] += 1
    else:
        counts[1] += 1

counts = [0, 0]  # counts[0]: 0의 개수, counts[1]: 1의 개수
recursive_count(0, 0, N, counts)
print(f"{counts[0]}\n{counts[1]}")