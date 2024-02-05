from collections import deque

T = int(input())

for _ in range(T):
    actions = input()
    action_length = len(actions)
    n = int(input())
    numbers = input()
    is_reverse = False

    try:
        if n == 0:
            numbers = deque([])
        else:
            numbers = deque(list(map(int, numbers[1:-1].split(","))))
        for idx in range(action_length):
            if actions[idx] == 'R':
                is_reverse = not is_reverse
            elif actions[idx] == 'D':
                if is_reverse:
                    numbers.pop()
                else:
                    numbers.popleft()
    except:
        print("error")
        continue

    if is_reverse:
        numbers.reverse()
    print(str(list(numbers)).replace(" ", ""))


