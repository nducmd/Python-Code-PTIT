t = int(input())

while t > 0:
    str = input()
    num1 = str[0:2]
    num2 = str[-2:]
    if num1 == num2 :
        print("YES")
    else:
        print("NO")
    t -= 1