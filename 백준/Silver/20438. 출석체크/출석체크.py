import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().strip().split())
attendance =  [0] * (N + 3) # 3부터 N+2 까지 학생 번호

sleepy_students = set(map(int, input().strip().split())) # K명의 졸고있는 학생
get_code_students = set(map(int, input().strip().split())) # Q명의 코드를 받은 학생

# 코드를 받은 학생들에 대해 출석 처리
for student in get_code_students:
    if student not in sleepy_students:
        # 자기 번호부터 배수들 모두 출석 처리
        for next_student in range(student, N + 3, student):
            if next_student not in sleepy_students:
                attendance[next_student] = 1

# 누적합 계산
prefix_sum = [0] * (N + 3)
for i in range(3, N + 3):
    prefix_sum[i] = (prefix_sum[i - 1] + attendance[i])
    
# M개의 줄에 걸쳐 특정 구간에서 출석하지 않은 학생 수 출력
result = []
for _ in range(M):
    S, E = map(int, input().strip().split())
    
    absent_count = (E - S + 1) - (prefix_sum[E] - prefix_sum[S - 1])
    result.append(absent_count)

print("\n".join(map(str, result)))