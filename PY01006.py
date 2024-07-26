def checkLucky(str):
    for i in range (0, len(str)):
        if str[i] != '4' and str[i] != '7':
            return False
    return True

t = int(input())

while t > 0:
    number = input()
    if checkLucky(number):
        print("YES")
    else:
        print("NO")
    t -= 1