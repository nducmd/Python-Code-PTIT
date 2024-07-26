t = int(input())
m = {}
a = []
while t > 0:
    t -= 1
    a.append(input())

a.append("")
j = 0
i = 0
cnt = 0
while i < len(a):
    if a[i] == '':
        print(a[j], end = ': ')
        print(cnt-1)
        j = i+1
        cnt = 0
    else:
        cnt += 1
    i += 1
        
    
    
    

# 9
# Home/accommodation
# What kind of housing/accommodation do you live in?
# Who do you live with?
# How long have you lived there?

# Study
# Describe your education
# What is your area of specialization?
# Why did you choose to study that major?