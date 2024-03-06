K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]

def get_num(n):
    return sum(map(lambda x: x//n, LAN))

def binary_search(lin, lax):
    lid = (lin + lax) // 2
    
    if lin >= lid: return lid
    num = get_num(lid)
    
    if num < N:
        return binary_search(lin, lid - 1)
    elif num >= N:
        return binary_search(lid, lax)

def linear_search(n):
    num = get_num(n)
    while num >= N:
        n += 1
        num = get_num(n)
    return n - 1

print(linear_search(binary_search(1, max(LAN))))