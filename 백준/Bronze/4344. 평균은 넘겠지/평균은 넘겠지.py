import sys
input = sys.stdin.readline
C = int(input().strip())

result = []
for _ in range(C):
    scores = list(map(int, input().strip().split()))
    N = scores[0]
    students = scores[1:]
    
    avg = sum(students) / N
    over_students = 0
    for j in range(N):
        if students[j] > avg:
            over_students += 1
            
    result.append(f"{over_students / N * 100:.3f}%")

sys.stdout.write('\n'.join(map(str, result)))