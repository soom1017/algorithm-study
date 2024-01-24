N = int(input())
L = list(map(int, input().split()))
v = int(input())
print(sum([1 for i in L if i == v]))