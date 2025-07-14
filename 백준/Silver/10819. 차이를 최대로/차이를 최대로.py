import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().strip().split()))

result = 0
def solve(arr):
    answer = 0
    for i in range(len(arr)-1):
        temp_result = abs(arr[i] - arr[i+1])
        answer += temp_result
    
    return answer

for perm in permutations(A):
    answer = solve(perm)
    result = max(result, answer)

sys.stdout.write(str(result) + '\n')