import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input().strip())
graph = {}
result = []

for _ in range(N):
    current, left, right = map(str, input().strip().split())
    graph[current] = [left, right]

def recursive_preorder(graph, current, arr):
    # 기저 조건
    if current == '.':
        return
    
    arr.append(current)
    recursive_preorder(graph, graph[current][0], arr)
    recursive_preorder(graph, graph[current][1], arr)
    
    return arr
    
def recursive_inorder(graph, current, arr):
    # 기저 조건
    if current == '.':
        return
    
    recursive_inorder(graph, graph[current][0], arr)
    arr.append(current)
    recursive_inorder(graph, graph[current][1], arr)
    
    return arr

def recursive_postorder(graph, current, arr):
    # 기저 조건
    if current == '.':
        return
    
    recursive_postorder(graph, graph[current][0], arr)
    recursive_postorder(graph, graph[current][1], arr)
    arr.append(current)

    return arr

result.append(recursive_preorder(graph, 'A', []))
result.append(recursive_inorder(graph, 'A', []))
result.append(recursive_postorder(graph, 'A', []))

for i in range(3):
    sys.stdout.write(''.join(map(str, result[i])) + '\n')