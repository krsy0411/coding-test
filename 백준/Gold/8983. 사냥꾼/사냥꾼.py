import sys
input = sys.stdin.readline

M,N,L = map(int, input().strip().split())
sadae = list(map(int, input().split())) # 사대들의 x좌표
sadae.sort()

animals = [tuple(map(int, input().split())) for _ in range(N)]

# 바이너리 탐색 -> 동물을 잡을 수 있는지 체크
def is_possible_to_catch(x,y):
    # 수직 사정거리보다 높이 있는 경우 -> 불가능
    if y > L:
        return False
    
    start, end = 0, M-1 # 사대 배열의 시작과 끝 인덱스
    while start <= end:
        mid = (start + end) // 2
        
        if abs(x - sadae[mid]) <= L - y:
            return True
        elif sadae[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return False # 못 찾은 경우

result = 0
for x, y in animals:
    if is_possible_to_catch(x,y):
        result += 1
    
print(result)