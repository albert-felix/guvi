a = list(input())
b = list(a)
b[0] = a[-1]
b[-1] = a[0]
c = ''
for i in b:
    c +=i
print (c)
