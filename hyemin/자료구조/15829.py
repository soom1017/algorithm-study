L = int(input())
data = input().strip()
result = 0

for i in range(len(data)):
    num = ord(data[i]) - ord('a') + 1
    result += (num) * (31 ** i)

print(result % 1234567891)