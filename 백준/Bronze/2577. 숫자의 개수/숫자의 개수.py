import sys
input = sys.stdin.readline

A = int(input().strip())
B = int(input().strip())
C = int(input().strip())

counts = [0 for _ in range(10)]
value = str(A*B*C) # 순회를 위해 문자열로 변환
for x in value:
    counts[int(x)] += 1 # 각 숫자에 해당하는 인덱스의 카운트 증가

sys.stdout.write('\n'.join(map(str, counts)) + '\n')