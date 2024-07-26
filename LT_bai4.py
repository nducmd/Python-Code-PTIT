n = int(input())
for i in range(n):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    cnt5 = 0
    cnt6 = 0
    cnt7 = 0
    cnt8 = 0
    cnt9 = 0
    inp = list(map(int, input().split()))
    st = inp[0]
    en = inp[1]
    s = ""
    for j in range(st, en+1):
        s += str(j)

    cnt0 += s.count('0')
    cnt1 += s.count('1')
    cnt2 += s.count('2')
    cnt3 += s.count('3')
    cnt4 += s.count('4')
    cnt5 += s.count('5')
    cnt6 += s.count('6')
    cnt7 += s.count('7')
    cnt8 += s.count('8')
    cnt9 += s.count('9')    
    print(cnt0,cnt1, cnt2, cnt3, cnt4, cnt5, cnt6, cnt7, cnt8, cnt9)

