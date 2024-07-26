t = int(input())
while t > 0:
    t -= 1
    a = input()
    b = input()
    cnt = 0
    while a.find(b) != -1:
        i = a.find(b)
        cnt += 1
        a = a[0:i] + "_" + a[i+len(b):]
    
    print(cnt)