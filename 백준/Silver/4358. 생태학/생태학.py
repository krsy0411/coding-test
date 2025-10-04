import sys
input = sys.stdin.readline

data_set = {}
total_num = 0
while True:
    line = input()
    if not line:
        break
    
    tree_name = line.strip()
    data_set[tree_name] = data_set.get(tree_name, 0) + 1
    total_num += 1

# 사전순으로 정렬된 나무 이름 순서대로 출력
for tree_name in sorted(data_set.keys()):
    percentage = (data_set[tree_name] / total_num) * 100
    print(f"{tree_name} {percentage:.4f}")