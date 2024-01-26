# 문자열 화폐: https://acmicpc.net/problem/17828
n, x = map(int, input().split())

if n > x or x > n * 26:
    print('!')
elif x == n * 26:
    print('Z' * n)
else:
    # 앞은 A, 뒤는 Z를 깔고 사이 문자(k) 계산
    num_z = (x - n) // 25
    num_a = n - num_z - 1
    k = x - num_a - num_z * 26
    
    result = 'A' * num_a + chr(ord('A') - 1 + k) + 'Z' * num_z
    print(result)