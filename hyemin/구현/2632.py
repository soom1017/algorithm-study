# 골드2
import sys
from collections import defaultdict

input = sys.stdin.readline

# 하나의 피자만 사용해서 나올 수 있는 경우의 수 + 피자 두개를 모두 사용해서 만드는 경우의 수

target_pizza_size = int(input())
m, n = map(int, input().split())

a_pizza = [int(input()) for _ in range(m)]
b_pizza = [int(input()) for _ in range(n)]

def brute_force(pizza, pizza_length):
    cases = defaultdict(int)

    for i in range(pizza_length):
        # 피자 조각 배열이 1차원이므로 i부터 시작해서 i-1직전까지의 배열로 재배치
        tmp_pizza = pizza[i:] + pizza[:i]
       
        tmp_sum = 0
        for size in tmp_pizza:
            tmp_sum += size
            cases[tmp_sum] += 1
        
    cases[sum(pizza)] = 1

    return cases

cases_a = brute_force(a_pizza, m)
cases_b = brute_force(b_pizza, n)

number_of_cases = cases_a[target_pizza_size] + cases_b[target_pizza_size] # 피자 한판

for sum_size in cases_a:
    number_of_cases += cases_a[sum_size] * cases_b[target_pizza_size - sum_size]

print(number_of_cases)