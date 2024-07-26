dic = {}
dic[0] = 1
dic[1] = 1
dic[2] = 2
dic[3] = 6
dic[4] = 24
dic[5] = 120
dic[6] = 720
dic[7] = 5040
dic[8] = 40320
dic[9] = 362880
t = int(input())
while t > 0:
    t -= 1
    n = input()
    sum = 0
    for c in n:
        sum += dic[int(c)]
    print("Yes" if sum == int(n) else "No")