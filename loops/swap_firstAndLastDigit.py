a = input()
b = list(a)
b[0] = a[-1]
b[-1] = a[0]
print (*b, sep='')
