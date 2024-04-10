import sys
import bisect
input = sys.stdin.readline

N, M = map(int, input().split())

styles_names = []
styles_power = []

for _ in range(N):
    name, max_power = map(str, input().split())
    styles_names.append(name)
    styles_power.append(int(max_power))

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2
        
        if target <= arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return left

for _ in range(M):
    character_power = int(input())

    # idx = bisect.bisect_left(styles_power, character_power)
    idx = binary_search(styles_power, character_power)

    print(styles_names[idx])