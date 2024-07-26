import csv
with open("flights.csv") as file:
    doc = csv.reader(file)
    
    dulieu = list(doc)
    
t = int(input())
while t > 0:
    t -= 1
    a, b = input().split()
    sum = 0
    cnt = 0
    for i in dulieu[1:]:
        if i[4] == a and i[2] == b:
           sum += float(i[0])
           cnt += 1
           
    if sum == 0:
        print("Invaild")
    else:
        print("{:4f}".format(sum/cnt)) 