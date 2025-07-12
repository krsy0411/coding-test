import sys
input = sys.stdin.readline

peoples = [] # 난쟁이
total = 0 # 키 합
for _ in range(9):
    height = int(input().strip())
    total += height
    peoples.append(height)

for i in range(9-1):
    fake1, fake2 = 0,0
    for j in range(i+1, 9): 
        two_sum = peoples[i] + peoples[j]
        
        if((total - two_sum) == 100):
            fake1, fake2 = peoples[i], peoples[j]
    if fake1 and fake2:
        peoples.remove(fake1)
        peoples.remove(fake2)
        break

# 오름차순 정렬
peoples.sort()
for p in peoples:
    sys.stdout.write(str(p) + '\n')