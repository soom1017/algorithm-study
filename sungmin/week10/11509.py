N = int(input())
H = list(map(int, input().split()))
arrow = [0] * 1000001
for i in H:
    if arrow[i] > 0: arrow[i] -= 1
    arrow[i - 1] += 1
print(sum(arrow))