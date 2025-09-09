import sys
import bisect
input = sys.stdin.readline

N = int(input().strip())
sangeun_nums = list(map(int, input().strip().split()))
sangeun_nums.sort()

M = int(input().strip())
target_nums = list(map(int, input().strip().split()))

result = []
for target in target_nums:
    idx = bisect.bisect_left(sangeun_nums, target)

    # 이진 탐색을 통해 타겟이 존재하는지 확인
    if (idx < len(sangeun_nums) and (sangeun_nums[idx] == target)):
        result.append(1)
    else:
        result.append(0)

sys.stdout.write('\n'.join(map(str, result)))