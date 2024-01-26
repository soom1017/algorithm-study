# 설탕 배달: https://acmicpc.net/problem/2839
n = int(input())

m3 = 0
m5 = -1

for i in range(n // 5, -1, -1):
    if (n - i * 5) % 3 == 0:
        m5 = i
        m3 = int((n - m5 * 5) / 3)
        break

print(m3 + m5)