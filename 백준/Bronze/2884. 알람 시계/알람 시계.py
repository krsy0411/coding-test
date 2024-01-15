h, m = map(int,input().split())

if m>44:
    print(h, m-45)
elif h>=1 and m <=44:
    print(h-1, m+15)
else: # h=0인 경우
    print(23, m+15)