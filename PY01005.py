number = input()
cnt4 = 0
cnt7 = 0
for i in range (0, len(number)):
    if number[i] == '4':
        cnt4 += 1
    elif number[i] == '7':
        cnt7 += 1

if cnt4 + cnt7 == 4 or cnt4 + cnt7 == 7:
    print("YES")
else:
    print("NO")