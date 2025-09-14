import sys
input = sys.stdin.readline

n = int(input().strip())
# 총 26개의 알파벳
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for _ in range(n):
    line = input().strip()
    counts_dict = {char:0 for char in alphabet}
    
    for char in line:
        if char in counts_dict:
            counts_dict[char] += 1
    
    max_count = max(counts_dict.values())
    max_chars = [char for char, count in counts_dict.items() if count == max_count]
    
    if len(max_chars) > 1:
        print('?')
    else:
        print(max_chars[0])