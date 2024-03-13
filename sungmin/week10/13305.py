INF = 10e9
N = int(input())
WAY = list(map(int, input().split()))
CITY = list(map(int, input().split()))

city_len = len(CITY)
oil, spend, loc, min_cost = 0, 0, 0, CITY[0]
while loc < city_len - 1:
    cost = WAY[loc]
    min_cost = min(min_cost, CITY[loc])
    if oil < cost:
        spend += min_cost * (cost - oil)
        oil += cost - oil
    loc += 1
    oil -= cost
    
print(spend)
