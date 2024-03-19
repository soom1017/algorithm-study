import sys
input = sys.stdin.readline

N = int(input())
alphabets = {}

for _ in range(N):
    word = input().strip()
    word_len = len(word)

    for i in range(word_len):
        alphabet_order = ord(word[i]) - ord('A')
        if word[i] in alphabets:    
            alphabets[word[i]] += 10 ** (word_len - (i + 1))
        else:
            alphabets[word[i]] = 10 ** (word_len - (i + 1))

words_sorted = sorted(alphabets.values(), reverse=True)

result = 0

num = 9

for weight in words_sorted:
    result += weight * num
    num -= 1

print(result) 