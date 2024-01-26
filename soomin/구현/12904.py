# A와 B: https://acmicpc.net/problem/12904
s = input()
t = list(input())

able = False
s_len = len(s)

while s_len < len(t):
    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
    
    if ''.join(t) == s:
        able = True
        break
    
print(1 if able == True else 0)