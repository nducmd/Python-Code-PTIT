def check(s):
    if s[-3:] != '.py':
        return False
    for c in s:
        if not c.isalpha() and c != "_" and c != ".":
            return False
    return True

s = input().lower()

print("yes" if check(s) else "no")