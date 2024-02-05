same_rank = lambda stack : stack and stack[-1] != '('

s_list = list(input())
stack = list()

s_ret = ''
for c in s_list:
    if c == '(':
        stack.append(c)
    elif c == ')':
        while (same_rank(stack)):
            s_ret += stack.pop()
        stack.pop()
    elif 'A' <= c <= 'Z':
        s_ret += c
    elif c == '+' or c == '-':
        while (same_rank(stack)):
            s_ret += stack.pop() 
        stack.append(c)
    elif c == '*' or c == '/':
        # A+B*C*D/E
        # 아래 반복문이 없으면 : ABCDE/**+  A+(B*(C*(D/E)))
        # 아래 반복문이 있으면 : ABC*D*E/+  A+(((B*C)*D)/E)
        while (same_rank(stack) and (stack[-1] == "*" or stack[-1] =='/')):
            s_ret += stack.pop()
        stack.append(c)

stack.reverse()
s_ret += ''.join(stack)
print(s_ret)