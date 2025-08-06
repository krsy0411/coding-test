import sys
input = sys.stdin.readline

N = int(input().strip())

max_tip_result = 0 # 강호가 받을 수 있는 팁의 최댓값
tips = [int(input().strip()) for _ in range(N)]
tips.sort(reverse=True)
for i, tip in enumerate(tips):
    calculated_tip = (tip - i)
    max_tip_result += (calculated_tip if calculated_tip > 0 else 0)

print(max_tip_result)