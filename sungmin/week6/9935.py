s_list, ex = list(input()), input()
ex_len = len(ex)

stack = list()
for c in s_list:
    stack.append(c)
    if ''.join(stack[-ex_len:]) != ex:
        continue
    # 시간 초과 : stack = stack[:-ex_len]
    for _ in range(ex_len):
        stack.pop()

print(''.join(stack)) if stack else print('FRULA')