n, money = map(int, input().split())   #동전 종류와 가진 돈
wallet = []				#동전 담을 지갑 리스트

for i in range(n):			#동전 종류 만큼 반복할건데
    coin = int(input())			#가진 동전의 값 입력하고
    wallet.append(coin)			#지갑 리스트에 추가합니다.

wallet.reverse()	#가격을 오름차순으로 적기 때문에 내림차순으로 바꿔줍니다

count=0				#동전 개수를 구하는 것이 조건

for coin in wallet:			#지갑 리스트에서
        count = count + money // coin	#코인으로 나눈 몫이 동전의 개수
        money = money%coin		#잔돈은 나머지

print(count)			#동전의 개수 출력