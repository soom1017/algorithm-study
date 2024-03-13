for _ in range(int(input())):
    data = input()
    stack = []
    for ch in data:
        if ch == '(': # '('가 입력됨
            stack.append(ch)
        else: # ')'가 입력됨
            if len(stack) == 0: # 괄호 매칭이 안된 경우, 루프 탈출
                stack.append(ch)
                break
            else:
                last_ch = stack.pop()
                if last_ch == ')': # 괄호 매칭이 안된 경우, 루프 탈출
                    stack.append(ch)
                    break
        
    print('YES' if len(stack) == 0 else 'NO')