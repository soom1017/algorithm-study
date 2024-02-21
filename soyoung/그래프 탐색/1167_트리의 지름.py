import sys
sys.setrecursionlimit(10**6)

def add_star(LEN):
    if LEN == 1:
        return ['*']

    Stars = add_star(LEN//3) 
    L = []  
    
    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
    for S in Stars:
        L.append(S*3)
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(add_star(n)))