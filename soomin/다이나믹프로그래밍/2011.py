# 암호코드: https://www.acmicpc.net/problem/2011
data = list(map(int, input()))
len_data = len(data)

if data[0] == 0:
    print(0)
else:
    d = [0] * (len_data + 1)
    d[0] = 1
    d[1] = 1

    for i in range(2, len_data + 1):
        if data[i-1] > 0:
            d[i] = d[i-1]
        if 10 <= 10 * data[i-2] + data[i-1]  <= 26:
            d[i] += d[i-2]
        d[i] %= 1000000

    print(d[len_data])