import sys
input = sys.stdin.readline

N,S = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

def recursive_solve(depth, total):
	if depth == N:
		return 1 if total == S else 0
	
	return recursive_solve(depth+1, total + arr[depth]) + recursive_solve(depth+1, total)

result = recursive_solve(0, 0)
if S == 0:
	result -= 1
	
print(result)