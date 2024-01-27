# 단어 수학: https://www.acmicpc.net/problem/1339
n = int(input())

n_alphabets = ord('Z') - ord('A') + 1
alphabets = [0] * n_alphabets

for _ in range(n):
    word = input()
    for i in range(len(word)):
        idx = ord(word[i]) - ord('A')
        alphabets[idx] += 10 ** (len(word)-i-1)

alphabets.sort(reverse=True)
replaced = 9
result = 0
for fr in alphabets:
    if fr == 0:
        break
    result += replaced * fr
    replaced -= 1

print(result)