hour, minute = map(int, input().split())
timer = int(input())

h = (hour + ((minute + timer) // 60)) % 24
m = (minute + timer) % 60
print(h, m)