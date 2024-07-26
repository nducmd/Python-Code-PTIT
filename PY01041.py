def check2(n, i):
    for j in range (1,i+1):
        if n[j]<= n[j-1]:
            return False
    for j in range (i, len(n)-2):
        if n[j] <= n[j+1]:
            return False
    return True 
def check1(n):
    if len(n) < 3:
        return False
    for i in range(1,len(n)-1):
        if (check2(n, i)):
            return True
    return False

t = int(input())
while t > 0:
    n = input()
    print("YES" if check1(n) else "NO")
    t -= 1