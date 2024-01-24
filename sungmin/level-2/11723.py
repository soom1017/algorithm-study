import sys
input = sys.stdin.readline

ALL = list(range(1,21))
N = int(input())

s = set()
for _ in range(N):
    i = input().split()
    if i[0] == 'add':
        if int(i[1]) not in s: s.add(int(i[1]))
        
    elif i[0] == 'remove':
        if int(i[1]) in s: s.remove(int(i[1]))
        
    elif i[0] == 'check':
        if int(i[1]) in s: print(1)
        else : print(0)
        
    elif i[0] == 'toggle': 
        if int(i[1]) in s: s.remove(int(i[1]))
        else : s.add(int(i[1]))
        
    elif i[0] == 'all': 
        s.update(ALL)
        
    elif i[0] == 'empty': 
        s = set()
