import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

multi_tap = []
count = 0

for i, item in enumerate(arr):
    if item in multi_tap:
        continue
    
    if len(multi_tap) < N:
        multi_tap.append(item)
        continue
    else:
        plug_out_value = 0
        plug_out_index = -1
        count += 1
        
        temp = arr[i:]
        for x in multi_tap:
            if x in temp:
                target_index = temp.index(x)
                
                if plug_out_index < target_index:
                    plug_out_index = target_index
                    plug_out_value = x
            else:
                plug_out_value = x
                break
        multi_tap[multi_tap.index(plug_out_value)] = item
        
# 결과 출력
print(count)