inp = []

while True:
    try:
        inp = input().split()
        if not (inp[-1].endswith('.') or inp[-1].endswith('!') or inp[-1].endswith('?')):
            inp[-1] = inp[-1] + '.'
        print(inp[0].lower().title(), end = " ")
        is_begin = 0
        for i in range(1, len(inp)):
            s = inp[i].lower()
            if (s.endswith('.') or s.endswith('!') or s.endswith('?')):
                print(s)
                is_begin = 1
            else:
                if is_begin == 1:
                    print(s.title(), end = " ")
                    is_begin = 0
                else:
                    print(s, end = " ")
    except Exception:
        break