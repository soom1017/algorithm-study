for _ in range(int(input())):
    N = int(input())
    stock = list(map(int, input().split()))
    
    selling_date = list([0])
    for day in range(1, N):
        while selling_date and stock[selling_date[-1]] < stock[day]:
            selling_date.pop()
        selling_date.append(day)
    
    all_price = 0
    last_sell = -1
    for day in selling_date:
        all_price += stock[day] * (day - last_sell - 1) - sum(stock[last_sell + 1:day])
        last_sell = day
    
    print(all_price)
