import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

words_dict = {}

for _ in range(N):
    word = input().rstrip()
    
    if words_dict.get(word):
        words_dict[word][0] += 1
    else:
        length = len(word)
        if length >= M:
            words_dict[word] = [1, length]

sorted_dict = sorted(words_dict.items(), key = lambda item:(-item[1][0], -item[1][1], item[0]))

for key, value in sorted_dict:
    print(key)