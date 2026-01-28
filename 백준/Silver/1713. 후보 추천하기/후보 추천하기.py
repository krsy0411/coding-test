import sys
input = sys.stdin.readline

N = int(input())
total = int(input())
students = list(map(int, input().split()))

photos = {}
time = 0

for student in students:
    time += 1
    
    # 이미 사진틀에 있는 학생의 경우
    if student in photos:
        photos[student][0] += 1
        continue
    
    # 사진틀에는 없지만 사진틀 자리가 남은 경우
    if len(photos) < N:
        photos[student] = [1, time]
        continue
    
    # 사진틀이 가득 찬 경우 : 삭제가 필요한 경우
    # 추천수가 적고 오래된 학생을 딕셔너리에서 삭제
    delete_target = min(photos.items(), key=lambda x: (x[1][0], x[1][1]))
    del photos[delete_target[0]]
    
    photos[student] = [1, time]

result = sorted(photos.keys())
print(' '.join(map(str, result)))