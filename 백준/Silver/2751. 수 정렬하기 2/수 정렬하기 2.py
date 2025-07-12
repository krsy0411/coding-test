import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [int(input().strip()) for _ in range(N)]
arr.sort() # 정수 오름차순 정렬

sys.stdout.write('\n'.join(map(str, arr)) + '\n')