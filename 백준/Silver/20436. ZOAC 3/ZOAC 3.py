import sys

input = sys.stdin.readline

left_start, right_start = map(str, input().split())
word = input().strip()

keyboard = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
]

def find_position(char):
    for i in range(3):
        for j in range(len(keyboard[i])):
            if keyboard[i][j] == char:
                return (i, j)
    return None

def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

left_pos = find_position(left_start)
right_pos = find_position(right_start)
total_time = 0

for char in word:
    # 왼손으로 타이핑하는 문자
    if char in 'qwertasdfgzxcv':
        char_pos = find_position(char)
        total_time += distance(left_pos, char_pos) + 1
        left_pos = char_pos
    # 오른손으로 타이핑하는 문자
    else:
        char_pos = find_position(char)
        total_time += distance(right_pos, char_pos) + 1
        right_pos = char_pos

print(total_time)