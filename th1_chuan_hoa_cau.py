while True:
    try:
        inp = input().split()
        print(inp[0].lower().title(), end = " ")
        s = inp[-1]
        if not (s.endswith('.') or s.endswith('?') or s.endswith('!')):
            inp[-1] += '.'
        if len(s) == 1 and not (inp[-2].endswith('.') or inp[-2].endswith('?') or inp[-2].endswith('!')):
            inp[-2] += inp[-1]
            inp.pop()
        is_begin = 0
        for i in range(1, len(inp)):
            s = inp[i].lower()
            if (s.endswith('.') or s.endswith('?') or s.endswith('!')):
                print(s)
                is_begin = 1
            else:
                print(s, end = " ")
    except Exception:
        break