# 큰 수 만들기: https://www.acmicpc.net/problem/16496
n = int(input())
nums = input().split()
    
def foo():
    # 0이 정답인 경우, 0 하나만 출력
    if int(''.join(nums)) == 0:
        print(0)
        return

    # 앞의 숫자부터 비교하며 정렬하되, 자릿수가 차이나는 경우 34 > 3 > 32, 121 > 1211 순으로 올 수 있게.
    max_length = 0
    for num in nums:
        max_length = max(max_length, len(num))
    max_length *= 2

    data = []
    for i in range(n):
        # comparable: max_length까지 수 반복. 4321의 경우, 4321432143...
        length = len(nums[i])
        num_iter = max_length // length
        remains = max_length - num_iter * length

        comparable = int(nums[i] * num_iter + nums[i][:remains])
        data.append([nums[i], comparable])

    data.sort(reverse=True, key=lambda x: x[1])
    for i in range(n):
        print(data[i][0], end='')

foo()