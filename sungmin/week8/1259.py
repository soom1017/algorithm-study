while 1:
    flag = True

    c = input()
    if c == '0': break
    
    s, e = 0, len(c) - 1
    while s < e:
        if c[s] != c[e]:
            flag = False
        s += 1
        e -= 1
    
    print("yes") if flag else print("no")