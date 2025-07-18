import sys
input = sys.stdin.readline

N,C = map(int, input().strip().split())
X = [int(input().strip()) for _ in range(N)]
X.sort()

# 인접한 두 공유기 사이의 거리 : start,end는 최소/최대 거리값 의미
def binary_search(start, end):
    result = 0
    
    while start <= end:
        mid = (start + end) // 2 # 인접 공유기의 최대 거리 후보값
        count = 1 # 설치한 공유기 개수
        last_installed = X[0]
        
        for i in range(1,N):
            if X[i] - last_installed >= mid:
                count += 1
                last_installed = X[i]

        if count >= C:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

result = binary_search(1, X[-1] - X[0])
print(result)