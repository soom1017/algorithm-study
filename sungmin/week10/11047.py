N, K = map(int, input().split())
COINS = list()
for _ in range(N): COINS.append(int(input()))
amount = 0
for coin in reversed(COINS):
    amount += K // coin
    K = K % coin
print(amount)