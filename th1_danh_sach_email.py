contactList = open('CONTACT.in')
cL = set()
for line in contactList:
    s = line.strip()
    cL.add(s.lower())
    
lst = list(cL)
lst.sort()
for s in lst:
    print(s)