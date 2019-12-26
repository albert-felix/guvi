n = input()
a=''
frequency = {}
x = 0
s = 0

for i in n:
    if i not in a:
        a+=i
        
for i in a:
    for p in n:
        if a[x]==p:
            s+=1
    frequency[i] = s
    s = 0
    x += 1
    print ( i + ' --> ' + str(frequency[i]))
