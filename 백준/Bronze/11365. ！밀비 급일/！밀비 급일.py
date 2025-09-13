import sys

input = sys.stdin.readline

data = []
while True:
    s = input().strip()  # 입력의 한 줄에 해당

    if s == "END":
        break

    data.append(s[::-1])

sys.stdout.write("\n".join(data))