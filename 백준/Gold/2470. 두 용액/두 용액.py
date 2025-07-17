import sys
input = sys.stdin.readline

N = int(input().strip())
liquid = list(map(int, input().strip().split()))
liquid.sort()

def solve():
    # 두 용액을 가리키는 인덱스
    left = 0
    right = N - 1 
    min_sum = float('inf')
    result = (0, 0)

    while left < right:
        mixed_liquid = liquid[left] + liquid[right]

        if abs(mixed_liquid) < min_sum:
            min_sum = abs(mixed_liquid)
            result = (liquid[left], liquid[right])
            
        if mixed_liquid == 0:
            break
            
        if mixed_liquid < 0:
            left += 1
        else:
            right -= 1

    return result

liquid1, liquid2 = solve()
print(f"{liquid1} {liquid2}")