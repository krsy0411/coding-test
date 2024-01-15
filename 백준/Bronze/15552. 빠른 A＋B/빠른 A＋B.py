import sys

t = int(sys.stdin.readline()) #input()사용가능
for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)