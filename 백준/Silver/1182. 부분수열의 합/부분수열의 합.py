import sys
input = sys.stdin.readline

N, S = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
count = 0

def solve_recursive(current_sum, depth):
    global count
    
    if depth == N:
        if current_sum == S:
            count += 1
        return

    solve_recursive(current_sum + arr[depth], depth + 1) # 포함
    solve_recursive(current_sum, depth + 1) # 포함X

solve_recursive(0,0)

# S가 0인 경우 : 첫 시점에 아무것도 선택하지 않은 경우도 하나의 부분수열로 간주되므로
if S == 0:
    count -= 1

sys.stdout.write(f"{count}\n")