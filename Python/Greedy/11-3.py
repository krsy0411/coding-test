s = input()
# 몇 번 뒤집어야 하는가? -> 횟수만 알아내면 됨

result = 0
cnt = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1

print((cnt+1) // 2)
