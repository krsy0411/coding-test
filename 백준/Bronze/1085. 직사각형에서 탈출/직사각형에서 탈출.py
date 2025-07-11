import sys
input = sys.stdin.readline
x,y,w,h = list(map(int, input().split()))

result = min(x,w-x,y,h-y)
sys.stdout.write(str(result))