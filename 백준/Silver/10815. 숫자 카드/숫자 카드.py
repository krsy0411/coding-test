import sys
input = sys.stdin.readline

N = int(input().strip())
sangeun_nums = set(map(int, input().strip().split()))

M = int(input().strip())
target_nums = list(map(int, input().strip().split()))

result = []
for target in target_nums:
    if target in sangeun_nums:
        result.append(1)
    else:
        result.append(0)

sys.stdout.write('\n'.join(map(str, result)))