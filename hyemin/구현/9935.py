data = input().strip()
explosion = input().strip()

# while explosion in data:
#     data = data.replace(explosion, "")

# if data:
#     print(data)
# else:
#     print("FRULA")

stack = []
expl_len = len(explosion)

for ch in data:
    stack.append(ch)
    if ch == stack[-1] and ''.join(stack[-expl_len:]) == explosion:
        del stack[-expl_len:]

print(''.join(stack) if stack else 'FRULA')