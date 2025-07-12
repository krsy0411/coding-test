import sys
input = sys.stdin.readline

W,H = list(map(int, input().strip().split()))
T = int(input().strip()) # 자르는 횟수

cutline_w = [0,W] # 세로가 나뉘어질때
cutline_h = [0,H] # 가로가 나뉘어질때
for _ in range(T):
    line, num = list(map(int, input().strip().split()))
    if(line == 0):
        cutline_h.append(num)
    else:
        cutline_w.append(num)
cutline_w.sort()
cutline_h.sort()

max_width = 0
max_height = 0
for i in range(len(cutline_w)-1):
    temp_height = cutline_w[i+1] - cutline_w[i]
    if temp_height > max_height:
        max_height = temp_height
for i in range(len(cutline_h)-1):
    temp_width = cutline_h[i+1] - cutline_h[i]
    if temp_width > max_width:
        max_width = temp_width

sys.stdout.write(str(max_width * max_height) + '\n')