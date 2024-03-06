N = int(input())
two, five = 0, 0

for n in range(1, N + 1):
    while n and not n % 2:
        two += 1
        n //= 2
    while n and not n % 5:
        five += 1
        n //= 5

print(min(two, five))