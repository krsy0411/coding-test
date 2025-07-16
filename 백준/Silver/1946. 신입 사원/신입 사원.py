import sys
input = sys.stdin.readline

T = int(input().strip())
result = []

for _ in range(T):
    N = int(input().strip())
    applicants = []
    max_num = 0 # 각 테스트 케이스 별 선발 가능한 신입사원의 최대 인원수

    for i in range(N):
        first, second = map(int, input().strip().split())
        applicants.append((first, second))
    
    applicants.sort(key=lambda x: x[0])
    min_score = float('inf')  # 두 번째 면접 점수의 최솟값

    for first, second in applicants:
        if second < min_score:
            min_score = second
            max_num += 1

    result.append(max_num)
    
print('\n'.join(map(str, result)))