import sys
sys.setrecursionlimit(10**6)

arr = []
while True:
    try:
        x = int(sys.stdin.readline())
        arr.append(x)
    except:
        break

def post_order(start, end):
    if start > end:
        return
    root = arr[start]
    idx = start + 1
    while idx <= end and arr[idx] < root:
        idx += 1
    post_order(start + 1, idx - 1)
    post_order(idx, end)
    print(root)

post_order(0, len(arr) - 1)