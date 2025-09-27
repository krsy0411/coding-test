import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input().strip()) # 2^k (1 <= k <= 7)
paper = [list(map(int, input().strip().split())) for _ in range(N)] # 0 : 하얀색, 1 : 파란색

# 잘린 종이의 개수를 세는 변수 : 하얀색 종이, 파란색 종이
white_count = 0
blue_count = 0

def calculate_counts(x, y, size):
    global white_count, blue_count
    
    # 현재 사이즈에서 모든 색이 동일한지 확인
    initial_color = paper[x][y]
    all_same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != initial_color:
                all_same = False
                break
        if not all_same:
            break
    
    # 모두 동일한 색이라면 해당 색의 종이 개수 증가
    if all_same:
        if initial_color == 0:
            white_count += 1
        else:
            blue_count += 1
    # 색이 섞인 경우 : 4등분하여 재귀 호출
    else:
        half_size = size // 2
        calculate_counts(x, y, half_size) # 1사분면
        calculate_counts(x, y + half_size, half_size) # 2사분면
        calculate_counts(x + half_size, y, half_size) # 3사분면
        calculate_counts(x + half_size, y + half_size, half_size) # 4사분면

# 함수 실행 & 결과 출력
calculate_counts(0, 0, N)
sys.stdout.write(f"{white_count}\n{blue_count}\n")