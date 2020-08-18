a,b,c = map(int,input().split())

if a>b and a>c:
    if a**2 == (b**2 + c**2):
        print('yes')
    else:
        print('no')

elif b>a and b>c:
    if b**2 == (a**2 + c**2):
        print('yes')
    else:
        print('no')
        
else:
    if c**2 == (a**2 + b**2):
        print('yes')
    else:
        print('no')
