t = int(input())
for i in range(t):
    
    s1 = input()
    s2 = input()
    x1 = list(s1)
    x2 = list(s2)
    x1.sort(key = lambda x : ord(x))
    x2.sort(key = lambda x : ord(x))
    print(f"Test {i+1}: ", end = "")
    print('YES' if x1 == x2 else 'NO')
    
# 4
# testing
# intestg
# abc
# aabbbcccc
# abcabcbcc
# aabbbcccc
# abc
# xyz