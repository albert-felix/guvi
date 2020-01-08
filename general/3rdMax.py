n = int(input('Enter n value : '))
values = []

for i in range(0,n):
    values.append(int(input()))
    
a = 0
b = 0
c = 0

for i in values:
    if i == a:
        continue
    elif i > a:
        c = b
        b = a
        a = i
    elif i == b:
        continue
    elif i > b:
        c = b
        b = i
    elif i == c:
        continue
    elif i > c:
        c = i
print(c)

        
        
