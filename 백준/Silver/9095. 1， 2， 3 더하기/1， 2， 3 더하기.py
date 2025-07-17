#  백준 9095 : 1, 2, 3 더하기
import sys
input = sys.stdin.readline

T = int(input().strip())
result = []

# 재귀함수 작성 : 1,2,3의 합으로 n을 만들 수 있는 경우의 수를 구하는 함수(dp 사용 X)
def solve_recursive(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return solve_recursive(n - 1) + solve_recursive(n - 2) + solve_recursive(n - 3)

for _ in range(T):
    n = int(input().strip())
    result.append(solve_recursive(n))

sys.stdout.write('\n'.join(map(str, result)) + '\n')