import sys
input = sys.stdin.readline

N,M = map(int, input().strip().split())
trees = list(map(int, input().strip().split()))

# 집으로 들고갈 나무의 높이 구하기
def get_total_height(trees, h):
    total = 0
    
    for tree in trees:
        if tree > h:
            total += tree - h # 설정한 높이보다 큰 나무의 길이만큼 더하기
            
    return total

# 이진 탐색을 통해 나무 자르기
def binary_search(trees, M):
    start, end = 0, max(trees)
    result = 0
    
    while start <= end:
        mid = (start + end) // 2 # 중간 높이 계산
        total_height = get_total_height(trees, mid)
        
        if total_height >= M:
            result = mid  # 현재 높이로 자른 나무의 길이가 M 이상이면 결과 갱신
            start = mid + 1
        else:
            end = mid - 1
    
    return result

result = binary_search(trees, M)
print(result)