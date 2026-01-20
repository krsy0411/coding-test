import sys
input = sys.stdin.readline

MAX_COUNT = 5
MAX_LENGTH = 15

result = ''
arr = []
for _ in range(MAX_COUNT):
    line = input().strip()
    arr.append(line)

for i in range(MAX_LENGTH):
    for j in range(MAX_COUNT):
        if i < len(arr[j]):
            result += arr[j][i]
    
sys.stdout.write(result)