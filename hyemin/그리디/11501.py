T = int(input())

for _ in range(T):
    days = int(input())
    stocks = list(map(int, input().split()))

    stocks.reverse()
    max_stock = stocks[0]

    profit_sum = 0

    for i in range(1, days):
        if max_stock < stocks[i]: # 주가가 기존의 최대 주가보다 높은 경우 max값 갱신
            max_stock = stocks[i]
        else:
            profit_sum += max_stock - stocks[i] # 미래의 max stock들이 더 큰 경우 판매
    
    print(profit_sum)