n = int(input())

#1부터 n까지 반복
for i in range(1, n+1):
    print(" "*(n-i) + "*"*i)