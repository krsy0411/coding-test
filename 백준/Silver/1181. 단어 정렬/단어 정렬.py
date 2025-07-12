import sys
input = sys.stdin.readline

N = int(input().strip())
jiphap = set()
for _ in range(N):
    word = input().strip()
    jiphap.add(word)

sorted_jiphap = sorted(jiphap, key = lambda x: (len(x), x))
sys.stdout.write('\n'.join(sorted_jiphap) + '\n')