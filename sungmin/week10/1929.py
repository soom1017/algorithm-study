M, N = map(int, input().split())

sieve = list(range(2, N + 1)) # of Eratosthenes
sieve_len = len(sieve)
prime = [1] * (2 + sieve_len)

for i in range(2, 2 + sieve_len):
    if not prime[i]: continue
    if i >= M: print(i)
    for i in range(i + i, 2 + sieve_len, i):
        prime[i] = 0
